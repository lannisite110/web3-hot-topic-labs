<script setup lang="ts">
import { computed, ref } from 'vue'
import { useLabSimulate } from '../../frontend/shared/useLabSimulate'
import { parseHints } from '../../frontend/shared/parseHints'

const didMethod = ref('did:demo:edu')
const disclosureLevel = ref('email')
const requestedClaim = ref('email')

const claimOptions = [
  { id: 'email', label: '披露邮箱 hash', public: 'email@demo.edu', withheld: 'sha256:email…redacted' },
  { id: 'age_over_18', label: '披露年龄区间', public: 'age>=18', withheld: 'sha256:exact-age…withheld' },
  { id: 'country', label: '披露国家代码', public: 'country=SG', withheld: 'sha256:passport…withheld' },
]

const selectedClaim = computed(() => claimOptions.find((c) => c.id === requestedClaim.value))

const { loading, error, result, taskStatus, taskReport, runSimulate, parseEvaluation } =
  useLabSimulate('edu.hot.did')

const evaluation = computed(() => parseEvaluation(result.value?.evaluation))
const hints = computed(() => parseHints(evaluation.value?.audit_hints))

const proofValid = computed(() => hints.value.proof_valid === 'true')

function submit() {
  runSimulate('Move 链上 DID 与选择性披露教学', {
    did_method: didMethod.value,
    disclosure_level: disclosureLevel.value,
    requested_claim: requestedClaim.value,
  })
}
</script>

<template>
  <section class="lab-panel">
    <header class="lab-header">
      <img src="/assets/icon.png" alt="" width="32" height="32" />
      <div>
        <h1>DID 隐私演示</h1>
        <p class="muted">选择性披露 · Move 教学 · 测试网 only</p>
      </div>
    </header>

    <div class="lab-grid">
      <div class="card">
        <h2>身份与披露策略</h2>
        <label>DID 方法 <input v-model="didMethod" /></label>
        <label>
          披露级别
          <select v-model="disclosureLevel">
            <option value="email">标准披露</option>
            <option value="minimal">最小披露</option>
            <option value="none">不披露（仅 hash 验证）</option>
          </select>
        </label>
        <label>
          请求验证的 claim
          <select v-model="requestedClaim">
            <option v-for="c in claimOptions" :key="c.id" :value="c.id">{{ c.label }}</option>
          </select>
        </label>
        <button :disabled="loading" @click="submit">{{ loading ? '验证中…' : '提交披露证明仿真' }}</button>
        <p v-if="taskStatus" class="status">任务: {{ taskStatus }}</p>
        <p v-if="error" class="error">{{ error }}</p>
      </div>

      <div class="card">
        <h2>披露视图</h2>
        <p v-if="selectedClaim"><strong>公开字段</strong>: {{ hints.revealed_field ?? selectedClaim.public }}</p>
        <p><strong>保留 hash</strong>: <code>{{ hints.withheld_hash ?? selectedClaim?.withheld }}</code></p>
        <p v-if="hints.claim_hash"><strong>claim hash</strong>: <code>{{ hints.claim_hash }}</code></p>
        <p class="proof" :class="{ ok: proofValid, bad: !proofValid && result }">
          证明: {{ proofValid ? '有效 ✓' : result ? '无效 ✗' : '待提交' }}
        </p>
      </div>

      <div class="card">
        <h2>选择性披露原理</h2>
        <ol class="flow">
          <li>用户注册 DID + 存 disclosed / withheld hash</li>
          <li>验证方仅请求必要 claim</li>
          <li>链上返回 disclosed 字段，不泄露 withheld 原文</li>
          <li>零知识/ hash 证明可扩展（教学简化）</li>
        </ol>
        <p class="muted">Move: <code>DidPrivacy.move</code></p>
      </div>
    </div>

    <details v-if="taskReport || result" class="raw">
      <summary>任务报告 JSON</summary>
      <pre>{{ JSON.stringify(taskReport ?? result, null, 2) }}</pre>
    </details>
  </section>
</template>

<style scoped>
.lab-panel { padding: 1rem; }
.lab-header { display: flex; gap: 0.75rem; align-items: center; margin-bottom: 1rem; }
.lab-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; }
.card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 1rem; }
.card h2 { margin: 0 0 0.75rem; font-size: 1rem; }
label { display: block; margin-bottom: 0.5rem; font-size: 0.875rem; }
input, select { display: block; width: 100%; margin-top: 0.25rem; padding: 0.45rem; border: 1px solid #cbd5e1; border-radius: 4px; }
.proof { font-weight: 600; margin-top: 0.75rem; }
.proof.ok { color: #15803d; }
.proof.bad { color: #dc2626; }
.flow { padding-left: 1.25rem; margin: 0; }
.flow li { margin-bottom: 0.35rem; }
.muted { color: #64748b; font-size: 0.875rem; }
code { font-family: monospace; font-size: 0.78rem; word-break: break-all; }
.status { color: #2563eb; font-size: 0.875rem; margin-top: 0.5rem; }
.error { color: #dc2626; }
button { margin-top: 0.5rem; padding: 0.5rem 1rem; width: 100%; background: #2563eb; color: #fff; border: none; border-radius: 4px; cursor: pointer; }
button:disabled { opacity: 0.6; }
.raw { margin-top: 1rem; }
.raw pre { background: #1e293b; color: #e2e8f0; padding: 1rem; border-radius: 8px; overflow: auto; font-size: 0.78rem; }
</style>
