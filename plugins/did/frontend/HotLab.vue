<script setup lang="ts">
import { computed, ref } from 'vue'
import { useLabI18n } from '@/composables/useLabI18n'
import { useLabSimulate } from '../../frontend/shared/useLabSimulate'
import { parseHints } from '../../frontend/shared/parseHints'

const PLUGIN_ID = 'edu.hot.did'
const { t, locale } = useLabI18n(PLUGIN_ID)

const didMethod = ref('did:demo:edu')
const disclosureLevel = ref('email')
const requestedClaim = ref('email')

const claimOptionDefs = [
  { id: 'email', key: 'claim_email', public: 'email@demo.edu', withheld: 'sha256:email…redacted' },
  { id: 'age_over_18', key: 'claim_age', public: 'age>=18', withheld: 'sha256:exact-age…withheld' },
  { id: 'country', key: 'claim_country', public: 'country=SG', withheld: 'sha256:passport…withheld' },
]

const claimOptions = computed(() => {
  void locale.value
  return claimOptionDefs.map((c) => ({
    ...c,
    label: t(c.key),
  }))
})

const selectedClaim = computed(() => claimOptionDefs.find((c) => c.id === requestedClaim.value))

const { loading, error, result, taskStatus, taskReport, runSimulate, parseEvaluation } =
  useLabSimulate(PLUGIN_ID)

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
        <h1>{{ t('title') }}</h1>
        <p class="muted">{{ t('subtitle') }}</p>
      </div>
    </header>

    <div class="lab-grid">
      <div class="card">
        <h2>{{ t('identitySection') }}</h2>
        <label>{{ t('didMethod') }} <input v-model="didMethod" /></label>
        <label>
          {{ t('disclosureLevel') }}
          <select v-model="disclosureLevel">
            <option value="email">{{ t('disclosure_email') }}</option>
            <option value="minimal">{{ t('disclosure_minimal') }}</option>
            <option value="none">{{ t('disclosure_none') }}</option>
          </select>
        </label>
        <label>
          {{ t('claimLabel') }}
          <select v-model="requestedClaim">
            <option v-for="c in claimOptions" :key="c.id" :value="c.id">{{ c.label }}</option>
          </select>
        </label>
        <button :disabled="loading" @click="submit">{{ loading ? t('verifying') : t('submitProof') }}</button>
        <p v-if="taskStatus" class="status">{{ t('task') }}: {{ taskStatus }}</p>
        <p v-if="error" class="error">{{ error }}</p>
      </div>

      <div class="card">
        <h2>{{ t('disclosureView') }}</h2>
        <p v-if="selectedClaim"><strong>{{ t('publicField') }}</strong>: {{ hints.revealed_field ?? selectedClaim.public }}</p>
        <p><strong>{{ t('withheldField') }}</strong>: <code>{{ hints.withheld_hash ?? selectedClaim?.withheld }}</code></p>
        <p v-if="hints.claim_hash"><strong>claim hash</strong>: <code>{{ hints.claim_hash }}</code></p>
        <p class="proof" :class="{ ok: proofValid, bad: !proofValid && result }">
          {{ t('proofStatus') }}: {{ proofValid ? t('proofValid') : result ? t('proofInvalid') : '—' }}
        </p>
      </div>

      <div class="card">
        <h2>{{ t('disclosureView') }}</h2>
        <ol class="flow">
          <li>{{ t('flow_1') }}</li>
          <li>{{ t('flow_2') }}</li>
          <li>{{ t('flow_3') }}</li>
          <li>{{ t('flow_4') }}</li>
        </ol>
        <p class="muted">Move: <code>DidPrivacy.move</code></p>
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
