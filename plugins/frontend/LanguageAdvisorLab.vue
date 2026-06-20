<script setup lang="ts">
import { computed, ref } from 'vue'
import { getPluginRegistry } from '@/plugins/loader'
import { useLabSimulate } from './shared/useLabSimulate'
import {
  LANGUAGE_LABELS,
  TOOLCHAIN_LABELS,
  normalizeAdvisorEvaluation,
} from './shared/advisorTypes'
import LabAssistDrawer from '@/components/LabAssistDrawer.vue'

const PLUGIN_ID = 'edu.hot.language-advisor'

const scenarios = [
  { id: 'defi', label: '通用 DeFi / DEX', prompt: '通用 DeFi swap lending staking dex' },
  { id: 'vault', label: '金库 / 高安全', prompt: 'vault treasury timelock 资金池 高安全' },
  { id: 'gas', label: 'Gas 优化 / 撮合', prompt: 'gas 优化 huff 撮合内核 高频' },
  { id: 'solana', label: 'Solana 高性能', prompt: 'solana anchor 高tps depin 链上订单簿' },
  { id: 'nft', label: 'NFT / Move 资产', prompt: 'nft move aptos sui 资产安全 防重放' },
  { id: 'zk', label: 'ZK Rollup', prompt: 'zk rollup cairo starknet 零知识 证明' },
  { id: 'btc', label: '比特币二层', prompt: 'bitcoin btc stacks clarity 比特币二层' },
  { id: 'game', label: '链游 / Cadence', prompt: 'flow cadence 链游 gamefi ip nft' },
  { id: 'pay', label: '合规支付 / TEAL', prompt: 'algorand teal pyteal 合规支付 极简' },
]

const selectedId = ref(scenarios[0].id)
const customPrompt = ref(scenarios[0].prompt)

const advise = useLabSimulate(PLUGIN_ID)
const compile = useLabSimulate(PLUGIN_ID)

const {
  loading: adviseLoading,
  error: adviseError,
  result: adviseResult,
  taskStatus: adviseTaskStatus,
  taskReport: adviseTaskReport,
  runSimulate: runAdviseSim,
} = advise

const {
  loading: compileLoading,
  error: compileError,
  taskStatus: compileTaskStatus,
  taskReport: compileTaskReport,
  runSimulate: runCompileSim,
} = compile

const activePrompt = computed(() => customPrompt.value.trim() || scenarios[0].prompt)

const evaluation = computed(() => {
  const raw = adviseResult.value?.evaluation
  if (typeof raw === 'string') {
    try {
      return normalizeAdvisorEvaluation(JSON.parse(raw))
    } catch {
      return null
    }
  }
  return normalizeAdvisorEvaluation(raw)
})

const suggestedLabMeta = computed(() => {
  const id = evaluation.value?.suggested_lab
  if (!id) return null
  return getPluginRegistry().find((p) => p.id === id) ?? null
})

function pickScenario(id: string) {
  selectedId.value = id
  const s = scenarios.find((x) => x.id === id)
  if (s) customPrompt.value = s.prompt
}

function runAdvise() {
  runAdviseSim(activePrompt.value, {
    scenario: activePrompt.value,
    tags: selectedId.value,
  })
}

function runCompile() {
  const lang = evaluation.value?.recommended_language ?? 'solidity'
  runCompileSim(
    `compile ${lang} template for teaching`,
    {
      language: lang,
      template: evaluation.value?.recommended_template,
      toolchain_group: evaluation.value?.toolchain_group,
    },
    { taskType: 'HOT_MULTI_LANG_COMPILE' },
  )
}
</script>

<template>
  <section class="advisor-panel">
    <header class="lab-header">
      <img src="/assets/icon.png" alt="" width="32" height="32" />
      <div>
        <h1>智能合约语言择优</h1>
        <p class="muted">edu.hot.language-advisor · 7 语言组 · 测试网教学 only</p>
      </div>
    </header>

    <div class="scenario-grid">
      <button
        v-for="s in scenarios"
        :key="s.id"
        type="button"
        class="scenario-chip"
        :class="{ active: selectedId === s.id }"
        @click="pickScenario(s.id)"
      >
        {{ s.label }}
      </button>
    </div>

    <div class="card">
      <label class="field">
        业务描述（可编辑）
        <textarea v-model="customPrompt" rows="3" placeholder="描述你的 DeFi / ZK / NFT 场景…" />
      </label>
      <div class="actions">
        <button class="primary" :disabled="adviseLoading" @click="runAdvise">
          {{ adviseLoading ? '分析中…' : '获取语言推荐' }}
        </button>
      </div>
      <p v-if="adviseTaskStatus" class="status">推荐任务: {{ adviseTaskStatus }}</p>
      <p v-if="adviseError" class="error">{{ adviseError }}</p>
    </div>

    <div v-if="evaluation?.compliance_passed" class="result-card">
      <h2>推荐结果</h2>
      <div class="badges">
        <span class="badge lang">{{ LANGUAGE_LABELS[evaluation.recommended_language ?? ''] ?? evaluation.recommended_language }}</span>
        <span v-if="evaluation.toolchain_group" class="badge chain">
          {{ TOOLCHAIN_LABELS[evaluation.toolchain_group] ?? evaluation.toolchain_group }}
        </span>
        <span v-if="evaluation.namespace" class="badge ns">{{ evaluation.namespace }}</span>
      </div>
      <p v-if="evaluation.reason" class="reason">{{ evaluation.reason }}</p>
      <p v-if="evaluation.recommended_template" class="template">
        入门模板: <code>{{ evaluation.recommended_template }}</code>
      </p>
      <div v-if="evaluation.tools?.length" class="tools">
        <span v-for="t in evaluation.tools" :key="t" class="tool-tag">{{ t }}</span>
      </div>
      <p v-if="evaluation.image" class="muted image-hint">Job 镜像: {{ evaluation.image }}</p>

      <div v-if="suggestedLabMeta" class="suggest-row">
        <div>
          <strong>建议下一步 Lab</strong>
          <p class="muted">{{ suggestedLabMeta.name }} ({{ suggestedLabMeta.id }})</p>
        </div>
        <a v-if="suggestedLabMeta" :href="suggestedLabMeta.routePrefix" class="secondary link-btn">
          打开专题 Lab →
        </a>
      </div>

      <div class="compile-row">
        <button
          type="button"
          class="primary outline"
          :disabled="compileLoading || !evaluation.recommended_language"
          @click="runCompile"
        >
          {{ compileLoading ? '编译任务提交中…' : '提交多语言编译 Job（HOT_MULTI_LANG_COMPILE）' }}
        </button>
        <p v-if="compileTaskStatus" class="status">编译任务: {{ compileTaskStatus }}</p>
        <p v-if="compileError" class="error">{{ compileError }}</p>
      </div>
    </div>

    <details v-if="compileTaskReport || adviseTaskReport" class="raw-json">
      <summary>任务报告 JSON</summary>
      <pre>{{ JSON.stringify(compileTaskReport ?? adviseTaskReport, null, 2) }}</pre>
    </details>

    <LabAssistDrawer
      plugin-id="edu.hot.language-advisor"
      :params="{ scenario: activePrompt, tags: selectedId }"
      :allowed-chain-ids="[11155111]"
      :audit-hints="evaluation?.audit_hints ?? []"
    />
  </section>
</template>

<style scoped>
.advisor-panel { padding: 1rem; max-width: 960px; }
.lab-header { display: flex; gap: 0.75rem; align-items: center; margin-bottom: 1.25rem; }
.muted { color: #64748b; font-size: 0.875rem; }
.scenario-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}
.scenario-chip {
  padding: 0.4rem 0.75rem;
  border-radius: 999px;
  border: 1px solid #cbd5e1;
  background: #fff;
  font-size: 0.85rem;
  cursor: pointer;
}
.scenario-chip.active {
  background: #2563eb;
  color: #fff;
  border-color: #2563eb;
}
.card, .result-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 1rem;
  margin-bottom: 1rem;
}
.result-card {
  background: linear-gradient(180deg, #f0fdf4 0%, #f8fafc 100%);
  border-color: #bbf7d0;
}
.result-card h2 { margin: 0 0 0.75rem; font-size: 1.1rem; }
.field { display: block; margin-bottom: 0.75rem; }
.field textarea {
  display: block;
  width: 100%;
  margin-top: 0.35rem;
  padding: 0.5rem;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  font-family: inherit;
}
.actions { display: flex; gap: 0.5rem; flex-wrap: wrap; }
.primary {
  padding: 0.55rem 1rem;
  background: #2563eb;
  color: #fff;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
.primary.outline {
  background: #fff;
  color: #2563eb;
  border: 1px solid #2563eb;
}
.primary:disabled, .secondary:disabled { opacity: 0.55; cursor: not-allowed; }
.secondary {
  padding: 0.45rem 0.85rem;
  background: #1e293b;
  color: #fff;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  white-space: nowrap;
  text-decoration: none;
  display: inline-block;
}
.badges { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.75rem; }
.badge {
  padding: 0.25rem 0.6rem;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: 600;
}
.badge.lang { background: #dbeafe; color: #1d4ed8; }
.badge.chain { background: #ede9fe; color: #5b21b6; }
.badge.ns { background: #fef3c7; color: #92400e; }
.reason { margin: 0 0 0.5rem; line-height: 1.5; }
.template code { font-size: 0.85em; word-break: break-all; }
.tools { display: flex; flex-wrap: wrap; gap: 0.35rem; margin: 0.75rem 0; }
.tool-tag {
  background: #e2e8f0;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  font-size: 0.8rem;
}
.suggest-row, .compile-row {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #e2e8f0;
}
.suggest-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}
.status { color: #0369a1; font-size: 0.875rem; margin-top: 0.5rem; }
.error { color: #dc2626; margin-top: 0.5rem; }
.image-hint { margin-top: 0.5rem; }
.raw-json { margin-top: 1rem; }
.raw-json pre {
  background: #1e293b;
  color: #e2e8f0;
  padding: 1rem;
  border-radius: 8px;
  overflow: auto;
  font-size: 0.78rem;
}
</style>
