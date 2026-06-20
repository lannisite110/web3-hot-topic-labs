# RWA 链上映射教学 · 分步实验

> **插件**: `edu.hot.rwa-edu` · **TaskType**: `HOT_RWA_EDU_SIM` · **Namespace**: `ns-hot-sim`  
> **合约**: `plugins/rwa-edu/contracts/RwaMappingDemo.sol`  
> **路线**: [HOT_TOPIC_LEARNING_PATH.md](../HOT_TOPIC_LEARNING_PATH.md) 第 5 步

---

## 学习目标

- 理解 **虚构资产** 链上映射教学模型  
- 明确本平台 **不做** 真实 RWA 发行/募资  

---

## 分步实验

### 步骤 1

打开 `/labs/edu.hot.rwa-edu`，填写虚构资产 ID（如 `DEMO-RWA-001`），提交仿真。

### 步骤 2：curl

```bash
curl -s -X POST http://127.0.0.1:8080/api/v1/labs/edu.hot.rwa-edu/simulate \
  -H 'Content-Type: application/json' \
  -d '{"user_prompt":"rwa edu mapping","params":{"asset_id":"DEMO-RWA-001"},"allowed_chain_ids":[11155111]}' \
  | jq '.evaluation'
```

---

## 合规边界

| 允许 | 禁止 |
|------|------|
| 虚构资产 ID 映射演示 | 真实资产代币化 / 募资 |
| 测试网 Solidity 模板 | 证券型代币发行 |

> **合规脚注**: testnet-only · 非 RWA 发行 · 虚构 asset only
