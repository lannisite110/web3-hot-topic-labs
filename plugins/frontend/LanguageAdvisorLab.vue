<script setup lang="ts">
import { ref } from 'vue'

const scenarios = [
  { label: '通用 DeFi / DEX', prompt: '通用 DeFi swap lending staking' },
  { label: '金库 / 高安全', prompt: 'vault treasury timelock 资金池 高安全' },
  { label: 'Gas 优化 / 撮合', prompt: 'gas 优化 huff 撮合内核' },
  { label: 'Solana 高性能', prompt: 'solana anchor 高tps depin' },
  { label: 'NFT / Move 资产', prompt: 'nft move aptos sui 资产安全' },
  { label: 'ZK Rollup', prompt: 'zk rollup cairo starknet 零知识' },
  { label: '比特币二层', prompt: 'bitcoin stacks clarity 比特币二层' },
  { label: '链游 / Cadence', prompt: 'flow cadence 链游 gamefi ip nft' },
  { label: '合规支付 / TEAL', prompt: 'algorand teal pyteal 合规支付' },
]

const selected = ref(scenarios[0].prompt)
const loading = ref(false)
const result = ref<Record<string, unknown> | null>(null)
const error = ref('')

async function runAdvise() {
  loading.value = true
  error.value = ''
  result.value = null
  try {
    const res = await fetch('/api/v1/labs/edu.hot.language-advisor/simulate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_prompt: selected.value,
        params: { scenario: selected.value },
        allowed_chain_ids: [11155111],
      }),
    })
    const data = await res.json()
    if (!res.ok) throw new Error(data.error || res.statusText)
    result.value = data
  } catch (e) {
    error.value = e instanceof Error ? e.message : String(e)
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <section class="card">
    <header class="header">
      <img src="/assets/icon.png" alt="" width="32" height="32" />
      <div>
        <h1>智能合约语言择优</h1>
        <p class="muted">edu.hot.language-advisor · 测试网教学 only</p>
      </div>
    </header>

    <label class="field">
      选择教学场景
      <select v-model="selected">
        <option v-for="s in scenarios" :key="s.label" :value="s.prompt">
          {{ s.label }}
        </option>
      </select>
    </label>

    <label class="field">
      业务描述
      <textarea v-model="selected" rows="3" />
    </label>

    <button class="primary" :disabled="loading" @click="runAdvise">
      {{ loading ? '分析中…' : '获取语言推荐' }}
    </button>

    <p v-if="error" class="error">{{ error }}</p>
    <pre v-if="result" class="result">{{ JSON.stringify(result, null, 2) }}</pre>
  </section>
</template>

<style scoped>
.header {
  display: flex;
  gap: 12px;
  align-items: center;
  margin-bottom: 16px;
}
.muted {
  color: #64748b;
  font-size: 0.875rem;
}
.field {
  display: block;
  margin-bottom: 12px;
}
.field select,
.field textarea {
  display: block;
  width: 100%;
  margin-top: 4px;
}
.primary {
  margin-top: 8px;
}
.error {
  color: #dc2626;
}
.result {
  margin-top: 16px;
  padding: 12px;
  background: #0f172a;
  color: #e2e8f0;
  border-radius: 8px;
  overflow: auto;
}
</style>
