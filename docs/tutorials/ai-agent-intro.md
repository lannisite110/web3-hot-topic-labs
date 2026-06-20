# AI Agent 受限沙箱 · 分步实验

> **插件**: `edu.hot.ai-agent` · **TaskType**: `HOT_AI_AGENT_SANDBOX` · **Namespace**: `ns-hot-sim`  
> **合约**: `plugins/ai-agent/contracts/AgentSandbox.sol`  
> **路线**: [HOT_TOPIC_LEARNING_PATH.md](../HOT_TOPIC_LEARNING_PATH.md) 第 5 步

---

## 学习目标

- 理解链上 Agent **权限边界**（最大动作次数等）  
- 区分「教学沙箱叙事」与真实 autonomous trading agent  

---

## 分步实验

### 步骤 1

打开 `/labs/edu.hot.ai-agent`，设置 **最大动作次数**（如 3），提交仿真。

### 步骤 2：curl

```bash
curl -s -X POST http://127.0.0.1:8080/api/v1/labs/edu.hot.ai-agent/simulate \
  -H 'Content-Type: application/json' \
  -d '{"user_prompt":"agent sandbox","params":{"max_actions":3},"allowed_chain_ids":[11155111]}' \
  | jq '.evaluation'
```

### 步骤 3：自检

- [ ] audit_hints 含 `max_actions=3`  
- [ ] 合规通过；无主网 RPC  

---

## 合规边界

| 允许 | 禁止 |
|------|------|
| 权限模型 / 沙箱教学 | 自主交易 / 抢跑 Agent |
| 虚构 Agent 策略 | 真实 LLM 密钥上链 |

> **合规脚注**: testnet-only · sandbox narrative only
