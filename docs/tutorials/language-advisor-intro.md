# 智能合约语言择优 — 操作教程

> **插件**: `edu.hot.language-advisor`  
> **合规**: 测试网 + 教学仿真 only

## 原理

平台根据用户描述的业务场景，匹配 `plugins/rules/language-choice-rules.yaml` 中的关键词规则，推荐最优合约语言与工具链组（EVM / Solana / Move / ZK 等）。

## 操作步骤

1. 在主库启动后端：`make run-rule-engine`、`make run-scheduler`、`make run-gateway`
2. 注册插件：`make register-plugins PLUGINS_DIR=..`
3. 打开前端 `/labs/edu.hot.language-advisor`，输入场景（如「通用 DeFi」「ZK Rollup」）
4. 点击「获取语言推荐」，查看 `evaluation.recommended_language` 与 `audit_hints`

## 联合调试（curl）

```bash
curl -X POST http://127.0.0.1:8080/api/v1/labs/edu.hot.language-advisor/simulate \
  -H 'Content-Type: application/json' \
  -d '{"user_prompt":"zk rollup cairo","params":{},"allowed_chain_ids":[11155111]}'
```

期望：`evaluation.compliance_passed=true`，`recommended_language=cairo`。

## 合规边界

| 允许 | 禁止 |
|------|------|
| 测试网部署演示 | 主网上线 |
| 语言/工具链教学推荐 | 真实交易策略 |
| 多语言编译 Job 仿真 | 生产级 Rollup 部署 |

---

> **合规脚注**: testnet-only · 虚构数据 only
