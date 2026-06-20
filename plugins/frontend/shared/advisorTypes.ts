/** Parsed language-advisor evaluation (from rule engine + audit_hints fallback). */

export interface AdvisorEvaluation {
  compliance_passed?: boolean
  recommended_language?: string
  recommended_template?: string
  rejection_reason?: string
  toolchain_group?: string
  tools?: string[]
  reason?: string
  suggested_lab?: string
  namespace?: string
  image?: string
  audit_hints?: string[]
}

export function hintMap(hints: string[] | undefined): Record<string, string> {
  const map: Record<string, string> = {}
  for (const line of hints ?? []) {
    const idx = line.indexOf('=')
    if (idx <= 0) continue
    map[line.slice(0, idx)] = line.slice(idx + 1)
  }
  return map
}

export function normalizeAdvisorEvaluation(raw: unknown): AdvisorEvaluation | null {
  if (!raw || typeof raw !== 'object') return null
  const e = raw as Record<string, unknown>
  const hints = e.audit_hints as string[] | undefined
  const hm = hintMap(hints)

  const toolsRaw = e.tools ?? hm.tools
  let tools: string[] | undefined
  if (Array.isArray(toolsRaw)) {
    tools = toolsRaw.map(String)
  } else if (typeof toolsRaw === 'string' && toolsRaw) {
    tools = toolsRaw.split(',').map((t) => t.trim())
  }

  return {
    compliance_passed: e.compliance_passed as boolean | undefined,
    recommended_language: (e.recommended_language as string) || undefined,
    recommended_template: (e.recommended_template as string) || undefined,
    rejection_reason: (e.rejection_reason as string) || undefined,
    toolchain_group: (e.toolchain_group as string) || hm.toolchain_group,
    tools,
    reason: (e.reason as string) || hm.match_reason,
    suggested_lab: (e.suggested_lab as string) || hm.suggested_lab,
    namespace: hm.namespace,
    image: hm.image,
    audit_hints: hints,
  }
}

export const LANGUAGE_LABELS: Record<string, string> = {
  solidity: 'Solidity',
  vyper: 'Vyper',
  huff: 'Huff',
  rust: 'Rust (Anchor)',
  move: 'Move',
  cairo: 'Cairo',
  clarity: 'Clarity',
  cadence: 'Cadence',
  teal: 'TEAL',
}

export const TOOLCHAIN_LABELS: Record<string, string> = {
  evm: 'EVM 工具链',
  solana: 'Solana 工具链',
  move: 'Move 工具链',
  zk: 'ZK / Cairo 工具链',
  btc: '比特币二层',
  flow: 'Flow / Cadence',
  algorand: 'Algorand / TEAL',
}
