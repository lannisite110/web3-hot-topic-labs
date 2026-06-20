<script setup lang="ts">
import { computed, ref } from 'vue'
import { useLabI18n } from '@/composables/useLabI18n'
import { useLabSimulate } from '../../frontend/shared/useLabSimulate'
import { parseHints } from '../../frontend/shared/parseHints'

const PLUGIN_ID = 'edu.hot.aa-wallet'
const { t, locale } = useLabI18n(PLUGIN_ID)

const owner = ref('0x0000000000000000000000000000000000000001')
const callData = ref('0xa9059cbb…transfer(demo)')
const currentStep = ref('build')

const flowStepIds = ['build', 'sign', 'bundle', 'validate', 'execute'] as const

const flowSteps = computed(() => {
  void locale.value
  return flowStepIds.map((id) => ({
    id,
    label: t(`flow_${id}`),
    desc: t(`flow_${id}_desc`),
  }))
})

const { loading, error, result, taskStatus, taskReport, runSimulate, parseEvaluation } =
  useLabSimulate(PLUGIN_ID)

const evaluation = computed(() => parseEvaluation(result.value?.evaluation))
const hints = computed(() => parseHints(evaluation.value?.audit_hints))

const completedSteps = computed(() => {
  const raw = hints.value.aa_flow_completed
  if (raw) return raw.split(',')
  if (taskStatus.value === 'completed') return [...flowStepIds]
  return [currentStep.value]
})

const userOpHash = computed(() => {
  void locale.value
  return hints.value.user_op_hash ?? t('userOpPending')
})

function selectStep(stepId: string) {
  currentStep.value = stepId
}

function submit() {
  runSimulate('ERC-4337 风格 AA 钱包测试网部署演示', {
    owner: owner.value,
    call_data: callData.value,
    aa_flow_step: currentStep.value,
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
        <h2>{{ t('userOpParams') }}</h2>
        <label>
          {{ t('ownerLabel') }}
          <input v-model="owner" />
        </label>
        <label>
          {{ t('callDataLabel') }}
          <input v-model="callData" />
        </label>
        <label>
          {{ t('stepLabel') }}
          <select v-model="currentStep">
            <option v-for="s in flowSteps" :key="s.id" :value="s.id">{{ s.label }}</option>
          </select>
        </label>
        <button :disabled="loading" @click="submit">
          {{ loading ? t('simulating') : t('submitAa') }}
        </button>
        <p v-if="taskStatus" class="status">{{ t('task') }}: {{ taskStatus }}</p>
        <p v-if="error" class="error">{{ error }}</p>
      </div>

      <div class="card span-2">
        <h2>{{ t('flowTitle') }}</h2>
        <div class="flow-track">
          <button
            v-for="(step, idx) in flowSteps"
            :key="step.id"
            type="button"
            class="flow-step"
            :class="{
              done: completedSteps.includes(step.id),
              current: currentStep === step.id,
            }"
            @click="selectStep(step.id)"
          >
            <span class="num">{{ idx + 1 }}</span>
            <div>
              <strong>{{ step.label }}</strong>
              <p class="muted">{{ step.desc }}</p>
            </div>
          </button>
        </div>
      </div>

      <div class="card">
        <h2>{{ t('userOpHash') }}</h2>
        <code class="hash">{{ userOpHash }}</code>
        <p v-if="hints.entry_point" class="muted">EntryPoint: {{ hints.entry_point }}</p>
        <p v-if="hints.owner" class="muted">Owner: {{ hints.owner }}</p>
        <p v-if="evaluation?.recommended_template" class="muted">
          {{ t('recommendedTemplate') }}: {{ evaluation.recommended_template }}
        </p>
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
.lab-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1rem;
}
.card.span-2 { grid-column: span 1; }
@media (min-width: 720px) {
  .card.span-2 { grid-column: span 2; }
}
.card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 1rem; }
.card h2 { margin: 0 0 0.75rem; font-size: 1rem; }
label { display: block; margin-bottom: 0.5rem; font-size: 0.875rem; }
input, select {
  display: block; width: 100%; margin-top: 0.25rem;
  padding: 0.45rem; border: 1px solid #cbd5e1; border-radius: 4px;
}
.flow-track { display: flex; flex-direction: column; gap: 0.5rem; }
.flow-step {
  display: flex; gap: 0.75rem; align-items: flex-start;
  text-align: left; padding: 0.65rem; border: 1px solid #e2e8f0;
  border-radius: 8px; background: #fff; cursor: pointer;
}
.flow-step.done { border-color: #86efac; background: #f0fdf4; }
.flow-step.current { border-color: #93c5fd; background: #eff6ff; box-shadow: 0 0 0 2px #bfdbfe; }
.flow-step .num {
  width: 1.75rem; height: 1.75rem; border-radius: 999px;
  background: #1e293b; color: #fff; display: flex; align-items: center; justify-content: center;
  font-size: 0.85rem; flex-shrink: 0;
}
.flow-step.done .num { background: #16a34a; }
.flow-step p { margin: 0.15rem 0 0; }
.hash { display: block; word-break: break-all; font-size: 0.78rem; color: #0f766e; margin: 0.5rem 0; }
.muted { color: #64748b; font-size: 0.875rem; }
.status { color: #2563eb; font-size: 0.875rem; margin-top: 0.5rem; }
.error { color: #dc2626; }
button:not(.flow-step) {
  margin-top: 0.5rem; padding: 0.5rem 1rem; width: 100%;
  background: #2563eb; color: #fff; border: none; border-radius: 4px; cursor: pointer;
}
button:disabled { opacity: 0.6; }
.raw { margin-top: 1rem; }
.raw pre { background: #1e293b; color: #e2e8f0; padding: 1rem; border-radius: 8px; overflow: auto; font-size: 0.78rem; }
</style>
