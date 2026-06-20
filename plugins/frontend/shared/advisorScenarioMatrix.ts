/** Static scenario ↔ language ↔ toolchain ↔ lab mapping (mirrors language-choice-rules.yaml). */

export interface ScenarioRow {
  id: string
  ruleId: string
  language: string
  toolchain: string
  namespace: string
  tools: string[]
  suggestedLab: string
  templateFile: string
}

export const SCENARIO_ROWS: ScenarioRow[] = [
  {
    id: 'defi',
    ruleId: 'defi-general',
    language: 'solidity',
    toolchain: 'evm',
    namespace: 'ns-evm',
    tools: ['solc', 'foundry'],
    suggestedLab: 'edu.hot.aa-wallet',
    templateFile: 'GenericDeFi.sol',
  },
  {
    id: 'vault',
    ruleId: 'vault-high-security',
    language: 'vyper',
    toolchain: 'evm',
    namespace: 'ns-evm',
    tools: ['vyper'],
    suggestedLab: 'edu.hot.rwa-edu',
    templateFile: 'Vault.vy',
  },
  {
    id: 'gas',
    ruleId: 'gas-hft-kernel',
    language: 'huff',
    toolchain: 'evm',
    namespace: 'ns-evm',
    tools: ['huff', 'foundry'],
    suggestedLab: 'edu.hot.mev',
    templateFile: 'MatchKernel.huff',
  },
  {
    id: 'solana',
    ruleId: 'solana-tps',
    language: 'rust',
    toolchain: 'solana',
    namespace: 'ns-solana',
    tools: ['rust', 'anchor'],
    suggestedLab: 'edu.hot.depin',
    templateFile: 'AnchorProgram.rs',
  },
  {
    id: 'nft',
    ruleId: 'nft-move-security',
    language: 'move',
    toolchain: 'move',
    namespace: 'ns-move',
    tools: ['aptos', 'sui'],
    suggestedLab: 'edu.hot.did',
    templateFile: 'NftAsset.move',
  },
  {
    id: 'zk',
    ruleId: 'zk-rollup',
    language: 'cairo',
    toolchain: 'zk',
    namespace: 'ns-hot-zk',
    tools: ['cairo', 'starknet-foundry'],
    suggestedLab: 'edu.hot.zk-modular',
    templateFile: 'ZkRollup.cairo',
  },
  {
    id: 'btc',
    ruleId: 'btc-l2',
    language: 'clarity',
    toolchain: 'btc',
    namespace: 'ns-lang-btc',
    tools: ['clarity'],
    suggestedLab: 'edu.hot.language-advisor',
    templateFile: 'BtcL2.clar',
  },
  {
    id: 'game',
    ruleId: 'gamefi-cadence',
    language: 'cadence',
    toolchain: 'flow',
    namespace: 'ns-lang-flow',
    tools: ['cadence'],
    suggestedLab: 'edu.hot.dao',
    templateFile: 'GameNFT.cdc',
  },
  {
    id: 'pay',
    ruleId: 'payment-teal',
    language: 'teal',
    toolchain: 'algorand',
    namespace: 'ns-lang-algorand',
    tools: ['pyteal', 'teal'],
    suggestedLab: 'edu.hot.language-advisor',
    templateFile: 'Payment.teal',
  },
]

export const TOOLCHAIN_GROUPS = [
  { id: 'evm', langs: 'Solidity · Vyper · Huff', namespace: 'ns-evm', output: '.bin / .abi / gas report' },
  { id: 'solana', langs: 'Rust (Anchor)', namespace: 'ns-solana', output: '.so program' },
  { id: 'move', langs: 'Move', namespace: 'ns-move', output: 'Move bytecode' },
  { id: 'zk', langs: 'Cairo', namespace: 'ns-hot-zk', output: 'Sierra / CASM' },
  { id: 'btc', langs: 'Clarity', namespace: 'ns-lang-btc', output: 'Clarity AST / deploy bundle' },
  { id: 'flow', langs: 'Cadence', namespace: 'ns-lang-flow', output: 'Cadence CDC' },
  { id: 'algorand', langs: 'TEAL / PyTEAL', namespace: 'ns-lang-algorand', output: 'TEAL template' },
] as const
