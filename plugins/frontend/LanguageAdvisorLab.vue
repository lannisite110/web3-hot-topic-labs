<script setup lang="ts">
import { computed, ref } from 'vue'
import { getPluginRegistry } from '@/plugins/loader'
import { useLabI18n } from '@/composables/useLabI18n'
import { useLabSimulate } from './shared/useLabSimulate'
import {
  LANGUAGE_LABELS,
  TOOLCHAIN_LABELS,
  normalizeAdvisorEvaluation,
} from './shared/advisorTypes'
import { SCENARIO_ROWS, TOOLCHAIN_GROUPS } from './shared/advisorScenarioMatrix'
import LabAssistDrawer from '@/components/LabAssistDrawer.vue'

const PLUGIN_ID = 'edu.hot.language-advisor'
const { t, locale } = useLabI18n(PLUGIN_ID)

const scenarios = computed(() => {
  void locale.value
  return SCENARIO_ROWS.map((row) => ({
    id: row.id,
    label: t(`scenario_${row.id}`),
    prompt: t(`scenario_${row.id}_prompt`),
    reason: t(`scenario_${row.id}_reason`),
    row,
  }))
})

const toolchainRows = computed(() => {
  void locale.value
  return TOOLCHAIN_GROUPS.map((g) => ({
    ...g,
    label: TOOLCHAIN_LABELS[g.id] ?? g.id,
    desc: t(`toolchain_${g.id}_desc`),
  }))
})

const matrixRows = computed(() => {
  void locale.value
  return SCENARIO_ROWS.map((row) => ({
    ...row,
    scenarioLabel: t(`scenario_${row.id}`),
    reason: t(`scenario_${row.id}_reason`),
    langLabel: LANGUAGE_LABELS[row.language] ?? row.language,
    chainLabel: TOOLCHAIN_LABELS[row.toolchain] ?? row.toolchain,
    labName: getPluginRegistry().find((p) => p.id === row.suggestedLab)?.name ?? row.suggestedLab,
  }))
})

const flowSteps = computed(() => {
  void locale.value
  return [1, 2, 3, 4, 5].map((n) => ({
    title: t(`flow_${n}_title`),
    desc: t(`flow_${n}_desc`),
  }))
})

const selectedId = ref(SCENARIO_ROWS[0].id)
const customPrompt = ref(t('scenario_defi_prompt'))

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

const activePrompt = computed(
  () => customPrompt.value.trim() || t(`scenario_${selectedId.value}_prompt`),
)

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

const matchedScenario = computed(() =>
  SCENARIO_ROWS.find((r) => r.language === evaluation.value?.recommended_language),
)

const suggestedLabMeta = computed(() => {
  const id = evaluation.value?.suggested_lab
  if (!id) return null
  return getPluginRegistry().find((p) => p.id === id) ?? null
})

const auditHintRows = computed(() => {
  const hints = evaluation.value?.audit_hints ?? []
  return hints.map((line) => {
    const idx = line.indexOf('=')
    if (idx <= 0) return { key: line, value: '' }
    return { key: line.slice(0, idx), value: line.slice(idx + 1) }
  })
})

function pickScenario(id: string) {
  selectedId.value = id
  customPrompt.value = t(`scenario_${id}_prompt`)
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
        <h1>{{ t('title') }}</h1>
        <p class="muted">{{ t('subtitle') }}</p>
      </div>
    </header>

    <article class="intro-card">
      <h2>{{ t('introTitle') }}</h2>
      <p class="intro-lead">{{ t('introLead') }}</p>
      <ul class="intro-stats">
        <li><strong>9</strong> {{ t('introStatScenarios') }}</li>
        <li><strong>7</strong> {{ t('introStatGroups') }}</li>
        <li><strong>9</strong> {{ t('introStatLanguages') }}</li>
        <li><strong>11</strong> {{ t('introStatLabs') }}</li>
      </ul>
      <p class="muted intro-note">{{ t('introNote') }}</p>
    </article>

    <details class="edu-panel" open>
      <summary>{{ t('toolchainTitle') }}</summary>
      <p class="panel-desc">{{ t('toolchainDesc') }}</p>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>{{ t('colGroup') }}</th>
              <th>{{ t('colLangs') }}</th>
              <th>{{ t('colNamespace') }}</th>
              <th>{{ t('colOutput') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="g in toolchainRows" :key="g.id">
              <td>
                <span class="cell-strong">{{ g.label }}</span>
                <span class="cell-sub">{{ g.desc }}</span>
              </td>
              <td><code>{{ g.langs }}</code></td>
              <td><code>{{ g.namespace }}</code></td>
              <td class="muted">{{ g.output }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </details>

    <details class="edu-panel" open>
      <summary>{{ t('matrixTitle') }}</summary>
      <p class="panel-desc">{{ t('matrixDesc') }}</p>
      <div class="table-wrap">
        <table class="data-table matrix-table">
          <thead>
            <tr>
              <th>{{ t('colScenario') }}</th>
              <th>{{ t('colLanguage') }}</th>
              <th>{{ t('colToolchain') }}</th>
              <th>{{ t('colSuggestedLab') }}</th>
              <th>{{ t('colReason') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="row in matrixRows"
              :key="row.id"
              class="matrix-row"
              :class="{ active: selectedId === row.id }"
              tabindex="0"
              @click="pickScenario(row.id)"
              @keydown.enter="pickScenario(row.id)"
            >
              <td>
                <span class="cell-strong">{{ row.scenarioLabel }}</span>
                <span class="cell-sub"><code>{{ row.ruleId }}</code></span>
              </td>
              <td>{{ row.langLabel }}</td>
              <td>{{ row.chainLabel }}</td>
              <td class="lab-cell">{{ row.labName }}</td>
              <td class="reason-cell">{{ row.reason }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </details>

    <section class="flow-card">
      <h3>{{ t('flowTitle') }}</h3>
      <ol class="flow-list">
        <li v-for="(step, i) in flowSteps" :key="i">
          <span class="flow-num">{{ i + 1 }}</span>
          <div>
            <strong>{{ step.title }}</strong>
            <p class="muted">{{ step.desc }}</p>
          </div>
        </li>
      </ol>
    </section>

    <h3 class="section-title">{{ t('tryTitle') }}</h3>
    <p class="muted section-hint">{{ t('tryHint') }}</p>

    <div class="scenario-grid">
      <button
        v-for="s in scenarios"
        :key="s.id"
        type="button"
        class="scenario-chip"
        :class="{ active: selectedId === s.id }"
        :title="s.reason"
        @click="pickScenario(s.id)"
      >
        <span class="chip-label">{{ s.label }}</span>
        <span class="chip-lang">{{ LANGUAGE_LABELS[s.row.language] ?? s.row.language }}</span>
      </button>
    </div>

    <div class="card">
      <label class="field">
        {{ t('promptLabel') }}
        <textarea v-model="customPrompt" rows="4" :placeholder="t('promptPlaceholder')" />
      </label>
      <p class="field-hint muted">{{ t('promptHint') }}</p>
      <div class="actions">
        <button class="primary" :disabled="adviseLoading" @click="runAdvise">
          {{ adviseLoading ? t('advising') : t('getAdvice') }}
        </button>
      </div>
      <p v-if="adviseTaskStatus" class="status">{{ t('adviseTask') }}: {{ adviseTaskStatus }}</p>
      <p v-if="adviseError" class="error">{{ adviseError }}</p>
    </div>

    <div v-if="evaluation?.compliance_passed" class="result-card">
      <h2>{{ t('resultTitle') }}</h2>
      <p v-if="matchedScenario" class="match-banner">
        {{ t('matchedRule') }}: <code>{{ matchedScenario.ruleId }}</code>
      </p>
      <div class="badges">
        <span class="badge lang">{{ LANGUAGE_LABELS[evaluation.recommended_language ?? ''] ?? evaluation.recommended_language }}</span>
        <span v-if="evaluation.toolchain_group" class="badge chain">
          {{ TOOLCHAIN_LABELS[evaluation.toolchain_group] ?? evaluation.toolchain_group }}
        </span>
        <span v-if="evaluation.namespace" class="badge ns">{{ evaluation.namespace }}</span>
      </div>
      <p v-if="evaluation.reason" class="reason">{{ evaluation.reason }}</p>
      <p v-if="evaluation.recommended_template" class="template">
        {{ t('starterTemplate') }}: <code>{{ evaluation.recommended_template }}</code>
      </p>
      <div v-if="evaluation.tools?.length" class="tools">
        <span v-for="tool in evaluation.tools" :key="tool" class="tool-tag">{{ tool }}</span>
      </div>
      <p v-if="evaluation.image" class="muted image-hint">{{ t('jobImage') }}: {{ evaluation.image }}</p>

      <details v-if="auditHintRows.length" class="hints-panel">
        <summary>{{ t('auditHintsTitle') }}</summary>
        <dl class="hints-dl">
          <template v-for="h in auditHintRows" :key="h.key">
            <dt>{{ h.key }}</dt>
            <dd><code>{{ h.value }}</code></dd>
          </template>
        </dl>
      </details>

      <div v-if="suggestedLabMeta" class="suggest-row">
        <div>
          <strong>{{ t('suggestNext') }}</strong>
          <p class="muted">{{ suggestedLabMeta.name }} ({{ suggestedLabMeta.id }})</p>
          <p class="path-hint muted">{{ t('pathHint') }}</p>
        </div>
        <a v-if="suggestedLabMeta" :href="suggestedLabMeta.routePrefix" class="secondary link-btn">
          {{ t('openLab') }}
        </a>
      </div>

      <div class="compile-row">
        <p class="compile-desc muted">{{ t('compileDesc') }}</p>
        <button
          type="button"
          class="primary outline"
          :disabled="compileLoading || !evaluation.recommended_language"
          @click="runCompile"
        >
          {{ compileLoading ? t('compileSubmitting') : t('compileJob') }}
        </button>
        <p v-if="compileTaskStatus" class="status">{{ t('compileTask') }}: {{ compileTaskStatus }}</p>
        <p v-if="compileError" class="error">{{ compileError }}</p>
      </div>
    </div>

    <details v-if="compileTaskReport || adviseTaskReport" class="raw-json">
      <summary>{{ t('taskReportJson') }}</summary>
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
.advisor-panel { padding: 1rem; max-width: 1024px; }
.lab-header { display: flex; gap: 0.75rem; align-items: center; margin-bottom: 1.25rem; }
.lab-header h1 { margin: 0; font-size: 1.35rem; color: #e8eef5; }
.muted { color: #8aa0b6; font-size: 0.875rem; line-height: 1.55; }

.intro-card {
  background: linear-gradient(135deg, #151b23 0%, #1a2433 100%);
  border: 1px solid #243044;
  border-radius: 12px;
  padding: 1.25rem 1.35rem;
  margin-bottom: 1rem;
}
.intro-card h2 { margin: 0 0 0.6rem; font-size: 1.05rem; color: #9ec5ff; }
.intro-lead { margin: 0 0 0.85rem; color: #c5d0de; line-height: 1.65; font-size: 0.92rem; }
.intro-stats {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem 1.25rem;
  margin: 0 0 0.75rem;
  padding: 0;
  list-style: none;
}
.intro-stats li {
  font-size: 0.85rem;
  color: #8aa0b6;
  background: #0f1419;
  border: 1px solid #243044;
  border-radius: 8px;
  padding: 0.35rem 0.75rem;
}
.intro-stats strong { color: #9ec5ff; font-size: 1rem; margin-right: 0.25rem; }
.intro-note { margin: 0; font-size: 0.82rem; }

.edu-panel {
  background: #151b23;
  border: 1px solid #243044;
  border-radius: 10px;
  padding: 0.75rem 1rem 1rem;
  margin-bottom: 1rem;
}
.edu-panel summary {
  cursor: pointer;
  font-weight: 600;
  color: #c5d0de;
  font-size: 0.95rem;
  padding: 0.25rem 0;
}
.panel-desc { margin: 0.5rem 0 0.75rem; font-size: 0.85rem; }

.table-wrap { overflow-x: auto; }
.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.82rem;
}
.data-table th,
.data-table td {
  text-align: left;
  padding: 0.55rem 0.65rem;
  border-bottom: 1px solid #243044;
  vertical-align: top;
}
.data-table th {
  color: #8aa0b6;
  font-weight: 600;
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}
.data-table td { color: #c5d0de; }
.data-table code {
  font-size: 0.78rem;
  color: #9ec5ff;
  background: #0f1419;
  padding: 0.1rem 0.35rem;
  border-radius: 4px;
}
.cell-strong { display: block; color: #e8eef5; font-weight: 600; }
.cell-sub { display: block; margin-top: 0.2rem; font-size: 0.78rem; color: #8aa0b6; }

.matrix-row { cursor: pointer; transition: background 0.12s; }
.matrix-row:hover { background: #1a2433; }
.matrix-row.active { background: #1a3a5c; }
.matrix-row.active td { color: #e8eef5; }
.reason-cell { max-width: 220px; line-height: 1.45; }
.lab-cell { font-size: 0.8rem; color: #9ec5ff !important; }

.flow-card {
  background: #151b23;
  border: 1px solid #243044;
  border-radius: 10px;
  padding: 1rem 1.15rem;
  margin-bottom: 1.25rem;
}
.flow-card h3 { margin: 0 0 0.75rem; font-size: 0.95rem; color: #c5d0de; }
.flow-list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
}
.flow-list li {
  display: flex;
  gap: 0.75rem;
  align-items: flex-start;
}
.flow-num {
  flex-shrink: 0;
  width: 1.5rem;
  height: 1.5rem;
  border-radius: 50%;
  background: #2563eb;
  color: #fff;
  font-size: 0.75rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
}
.flow-list strong { color: #e8eef5; font-size: 0.88rem; }
.flow-list p { margin: 0.15rem 0 0; }

.section-title { margin: 0 0 0.25rem; font-size: 1rem; color: #c5d0de; }
.section-hint { margin: 0 0 0.75rem; }

.scenario-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}
.scenario-chip {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 0.15rem;
  padding: 0.45rem 0.75rem;
  border-radius: 10px;
  border: 1px solid #243044;
  background: #151b23;
  font-size: 0.85rem;
  cursor: pointer;
  color: #c5d0de;
  min-width: 7.5rem;
}
.scenario-chip:hover { border-color: #2563eb; background: #1a2433; }
.scenario-chip.active {
  background: #1a3a5c;
  color: #e8eef5;
  border-color: #2563eb;
  box-shadow: 0 0 0 1px #2563eb;
}
.chip-label { font-weight: 600; }
.chip-lang { font-size: 0.72rem; color: #9ec5ff; opacity: 0.9; }
.scenario-chip.active .chip-lang { color: #bfdbfe; }

.card, .result-card {
  background: #151b23;
  border: 1px solid #243044;
  border-radius: 10px;
  padding: 1rem;
  margin-bottom: 1rem;
}
.result-card {
  background: linear-gradient(180deg, #0d2818 0%, #151b23 40%);
  border-color: #166534;
}
.result-card h2 { margin: 0 0 0.75rem; font-size: 1.1rem; color: #6ee7b7; }
.match-banner {
  margin: 0 0 0.75rem;
  font-size: 0.85rem;
  color: #8aa0b6;
}
.match-banner code { color: #9ec5ff; }

.field { display: block; margin-bottom: 0.35rem; color: #c5d0de; font-size: 0.9rem; }
.field textarea {
  display: block;
  width: 100%;
  margin-top: 0.35rem;
  padding: 0.6rem;
  border: 1px solid #243044;
  border-radius: 8px;
  font-family: inherit;
  background: #0f1419;
  color: #e8eef5;
  font-size: 0.88rem;
  line-height: 1.5;
  resize: vertical;
}
.field-hint { margin: 0 0 0.75rem; font-size: 0.8rem; }
.actions { display: flex; gap: 0.5rem; flex-wrap: wrap; }
.primary {
  padding: 0.55rem 1rem;
  background: #2563eb;
  color: #fff;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.88rem;
}
.primary.outline {
  background: transparent;
  color: #9ec5ff;
  border: 1px solid #2563eb;
}
.primary:disabled, .secondary:disabled { opacity: 0.55; cursor: not-allowed; }
.secondary {
  padding: 0.45rem 0.85rem;
  background: #2563eb;
  color: #fff;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  white-space: nowrap;
  text-decoration: none;
  display: inline-block;
  font-size: 0.85rem;
}
.badges { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.75rem; }
.badge {
  padding: 0.25rem 0.6rem;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: 600;
}
.badge.lang { background: #1a3a5c; color: #9ec5ff; }
.badge.chain { background: #2e1065; color: #c4b5fd; }
.badge.ns { background: #422006; color: #fcd34d; }
.reason { margin: 0 0 0.5rem; line-height: 1.55; color: #c5d0de; }
.template code { font-size: 0.85em; word-break: break-all; color: #9ec5ff; }
.tools { display: flex; flex-wrap: wrap; gap: 0.35rem; margin: 0.75rem 0; }
.tool-tag {
  background: #1e2733;
  border: 1px solid #243044;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  font-size: 0.8rem;
  color: #9ec5ff;
}
.hints-panel { margin-top: 0.75rem; }
.hints-panel summary { cursor: pointer; color: #8aa0b6; font-size: 0.85rem; }
.hints-dl {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 0.25rem 0.75rem;
  margin: 0.5rem 0 0;
  font-size: 0.8rem;
}
.hints-dl dt { color: #8aa0b6; }
.hints-dl dd { margin: 0; }
.hints-dl code { color: #9ec5ff; word-break: break-all; }

.suggest-row, .compile-row {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #243044;
}
.suggest-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}
.path-hint { margin: 0.25rem 0 0; font-size: 0.8rem; }
.compile-desc { margin: 0 0 0.5rem; }
.status { color: #38bdf8; font-size: 0.875rem; margin-top: 0.5rem; }
.error { color: #fca5a5; margin-top: 0.5rem; }
.image-hint { margin-top: 0.5rem; }
.raw-json { margin-top: 1rem; }
.raw-json summary { cursor: pointer; color: #8aa0b6; font-size: 0.85rem; }
.raw-json pre {
  background: #0f1419;
  color: #c5d0de;
  padding: 1rem;
  border-radius: 8px;
  overflow: auto;
  font-size: 0.78rem;
  border: 1px solid #243044;
}
</style>
