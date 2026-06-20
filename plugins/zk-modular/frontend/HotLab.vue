<script setup lang="ts">
import { computed, ref } from 'vue'
import { useLabI18n } from '@/composables/useLabI18n'
import { useLabSimulate } from '../../frontend/shared/useLabSimulate'
import { parseHints, hintNumber } from '../../frontend/shared/parseHints'

const PLUGIN_ID = 'edu.hot.zk-modular'
const { t, locale } = useLabI18n(PLUGIN_ID)

const batchSize = ref(8)
const { loading, error, result, taskStatus, taskReport, runSimulate, parseEvaluation } =
  useLabSimulate(PLUGIN_ID)

const evaluation = computed(() => parseEvaluation(result.value?.evaluation))
const hints = computed(() => parseHints(evaluation.value?.audit_hints))

const pipelineDefs = [
  { id: 'collect', icon: '📥' },
  { id: 'prove', icon: '⚡' },
  { id: 'submit', icon: '📦' },
  { id: 'anchor', icon: '🔗' },
]

const pipeline = computed(() => {
  void locale.value
  return pipelineDefs.map((step) => ({
    ...step,
    label: t(`pipeline_${step.id}`),
  }))
})

const demoBatches = computed(() => {
  const n = hintNumber(hints.value, 'batch_size', Number(batchSize.value) || 8)
  const root = hints.value.mock_batch_root ?? '0x…pending'
  return Array.from({ length: Math.min(n, 6) }, (_, i) => ({
    id: i + 1,
    txs: (Number(hints.value.tx_count) || n * 12) / n,
    root: i === n - 1 ? root : `0xbatch${i + 1}…demo`,
    status: i < n - 1 ? 'finalized' : taskStatus.value === 'completed' ? 'finalized' : 'proving',
  }))
})

const activeStep = computed(() => {
  if (taskStatus.value === 'completed') return 3
  if (taskStatus.value === 'running' || loading.value) return 2
  if (result.value) return 1
  return 0
})

function submit() {
  runSimulate('ZK 电路与 Rollup 批次提交教学仿真（测试网 mock verifier）', {
    batch_size: String(batchSize.value),
  })
}
</script>

<template>
  <section class="lab-panel">
    <header class="lab-header">
      <img src="/assets/icon.png" alt="" width="32" height="32" />
      <div>
        <h1>{{ t('title') }}</h1>
        <p class="muted">{{ t('subtitle') }}</p>
      </div>
    </header>

    <div class="lab-grid">
      <div class="card">
        <h2>{{ t('batchParams') }}</h2>
        <label>
          {{ t('batchSizeLabel') }}
          <input v-model.number="batchSize" type="number" min="1" max="64" />
        </label>
        <button :disabled="loading" @click="submit">
          {{ loading ? t('submitting') : t('submitBatch') }}
        </button>
        <p v-if="taskStatus" class="status">{{ t('task') }}: {{ taskStatus }}</p>
        <p v-if="error" class="error">{{ error }}</p>
      </div>

      <div class="card">
        <h2>{{ t('pipelineTitle') }}</h2>
        <ol class="pipeline">
          <li
            v-for="(step, idx) in pipeline"
            :key="step.id"
            :class="{ done: idx <= activeStep, current: idx === activeStep }"
          >
            <span class="step-icon">{{ step.icon }}</span>
            <strong>{{ step.label }}</strong>
          </li>
        </ol>
        <p v-if="hints.verifier" class="muted">Verifier: {{ hints.verifier }}</p>
      </div>

      <div class="card">
        <h2>{{ t('batchListTitle') }}</h2>
        <ul class="batch-list">
          <li v-for="b in demoBatches" :key="b.id">
            <div class="batch-row">
              <span>#{{ b.id }}</span>
              <span class="tag" :class="b.status">{{ t(`status_${b.status}`) }}</span>
            </div>
            <code>{{ b.root }}</code>
            <small class="muted">~{{ Math.round(b.txs) }} txs</small>
          </li>
        </ul>
        <p v-if="hints.l1_anchor" class="muted anchor">L1: {{ hints.l1_anchor }}</p>
      </div>
    </div>

    <details v-if="taskReport || result" class="raw">
      <summary>{{ t('taskReportJson') }}</summary>
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
.muted { color: #64748b; font-size: 0.875rem; }
.pipeline { list-style: none; padding: 0; margin: 0; }
.pipeline li {
  display: flex; align-items: center; gap: 0.5rem;
  padding: 0.5rem 0; border-left: 3px solid #e2e8f0; padding-left: 0.75rem; margin-bottom: 0.35rem;
}
.pipeline li.done { border-left-color: #22c55e; color: #15803d; }
.pipeline li.current { border-left-color: #2563eb; font-weight: 600; }
.step-icon { font-size: 1.1rem; }
.batch-list { list-style: none; padding: 0; margin: 0; }
.batch-list li { margin-bottom: 0.75rem; padding-bottom: 0.75rem; border-bottom: 1px solid #e2e8f0; }
.batch-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem; }
.tag { font-size: 0.75rem; padding: 0.15rem 0.45rem; border-radius: 4px; text-transform: uppercase; }
.tag.finalized { background: #dcfce7; color: #166534; }
.tag.proving { background: #dbeafe; color: #1d4ed8; }
code { font-family: monospace; font-size: 0.78rem; word-break: break-all; color: #0f766e; }
.status { color: #2563eb; font-size: 0.875rem; margin-top: 0.5rem; }
.error { color: #dc2626; }
.anchor { margin-top: 0.75rem; }
input { display: block; width: 100%; margin: 0.5rem 0; padding: 0.5rem; border: 1px solid #cbd5e1; border-radius: 4px; }
button { margin-top: 0.5rem; padding: 0.5rem 1rem; background: #2563eb; color: #fff; border: none; border-radius: 4px; cursor: pointer; }
button:disabled { opacity: 0.6; }
.raw { margin-top: 1rem; }
.raw pre { background: #1e293b; color: #e2e8f0; padding: 1rem; border-radius: 8px; overflow: auto; font-size: 0.78rem; }
</style>
