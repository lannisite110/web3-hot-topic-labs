# MEV PBS 博弈仿真 · 分步实验

> **插件**: `edu.hot.mev` · **TaskType**: `HOT_MEV_PBS_SIM` · **Namespace**: `ns-hot-sim`  
> **合约**: `plugins/mev/contracts/MevPbsAuction.sol` · **Job**: `k8s/overlays/ns-hot-sim/mev-job.yaml`  
> **路线**: [HOT_TOPIC_LEARNING_PATH.md](../HOT_TOPIC_LEARNING_PATH.md) 第 4 步

---

## 学习目标

- 理解 **Proposer-Builder Separation (PBS)** 教学模型  
- 区分「Builder 出价竞争 slot」与「MEV 套利机器人」（本平台禁止后者）  
- 阅读 `winning_builder` / `winning_bid_gwei` 规则输出  

---

## 前置条件

主库后端 + 前端 dev 已运行；插件已注册。

---

## 背景原理

以太坊 PBS 模式下，Builders 对区块 slot 出价，Proposer 选择最高 bid 并打包区块。本 Lab 使用 `MevPbsAuction.sol` 演示 `submitBid` / `selectWinningBuilder`，**非** 抢跑/三明治攻击教学。

---

## 分步实验

### 步骤 1：打开 Lab

`http://127.0.0.1:5173/labs/edu.hot.mev`

### 步骤 2：调整 PBS 参数

1. 设置 **区块槽位数**、**Builder 数量**、**slot 索引**  
2. 查看 Builder 出价表（演示排序）  
3. 点击 **运行 PBS 拍卖仿真**  

### 步骤 3：curl 验证

```bash
curl -s -X POST http://127.0.0.1:8080/api/v1/labs/edu.hot.mev/simulate \
  -H 'Content-Type: application/json' \
  -d '{
    "user_prompt": "PBS teaching",
    "params": { "block_slots": 12, "builder_count": 4, "slot_index": 2 },
    "allowed_chain_ids": [11155111]
  }' | jq '.evaluation'
```

**期望**：`recommended_template` 指向 `MevPbsAuction.sol`；hints 含 `pbs_mode=proposer-builder-separation`、`arbitrage_bot=forbidden`。

### 步骤 4：自检清单

- [ ] UI 显示 Proposer 选中的 builder  
- [ ] 合规：无「套利机器人」相关通过项  
- [ ] Job 报告（cluster 模式）含 solc 编译 gate 日志  

---

## K8s Job

`mev-job.yaml` 内联编译 PBS Solidity 片段 + `huff --version`（可选）。

---

## 相关链接

- 上一专题：[dao-intro.md](dao-intro.md)  
- 下一专题：[did-intro.md](did-intro.md)  

---

## 合规边界

| 允许 | 禁止 |
|------|------|
| PBS 算法 / 拍卖机制教学 | 主网 MEV 套利机器人 |
| 测试网仿真 | 生产 mempool 操控 |

> **合规脚注**: testnet-only · 非套利机器人 · 虚构 builder 数据
