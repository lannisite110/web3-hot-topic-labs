# DePIN 节点仿真 · 分步实验

> **插件**: `edu.hot.depin` · **TaskType**: `HOT_DEPIN_NODE_SIM` · **Namespace**: `ns-hot-sim`  
> **合约**: `plugins/depin/contracts/DepinNode.rs` (Anchor 模板)  
> **Job**: Solana toolchain gate · **路线**: [HOT_TOPIC_LEARNING_PATH.md](../HOT_TOPIC_LEARNING_PATH.md) 第 5 步

---

## 学习目标

- 理解 DePIN **节点注册** 叙事（Solana Anchor 方向）  
- 关联 language-advisor 对 Solana/depin 场景的 Rust 推荐  

---

## 分步实验

### 步骤 1

打开 `/labs/edu.hot.depin`，设置 **模拟节点数**，提交仿真。

### 步骤 2：curl

```bash
curl -s -X POST http://127.0.0.1:8080/api/v1/labs/edu.hot.depin/simulate \
  -H 'Content-Type: application/json' \
  -d '{"user_prompt":"depin node sim","params":{"node_count":5},"allowed_chain_ids":[11155111]}' \
  | jq '.evaluation'
```

### 步骤 3：K8s（可选）

`depin-job.yaml` 检查 `rustc` / `anchor` 版本。

---

## 合规边界

| 允许 | 禁止 |
|------|------|
| 测试网节点注册仿真 | 真实 DePIN 激励/代币经济 |
| 虚构 node_count | 主网设备挖矿 |

> **合规脚注**: testnet-only · devnet/sandbox nodes only
