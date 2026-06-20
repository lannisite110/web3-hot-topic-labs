# DAO 投票教学 · 分步实验

> **插件**: `edu.hot.dao` · **TaskType**: `HOT_DAO_VOTE_SIM` · **Namespace**: `ns-hot-sim`  
> **合约**: `plugins/dao/contracts/DaoVoteDemo.sol` · **Job**: `k8s/overlays/ns-hot-sim/dao-job.yaml`  
> **路线**: [HOT_TOPIC_LEARNING_PATH.md](../HOT_TOPIC_LEARNING_PATH.md) 第 4 步

---

## 学习目标

- 理解测试网 DAO 提案、投票计数与 quorum 概念  
- 使用 UI 本地点票后提交平台仿真  
- 阅读 `proposal_status` / `yes_votes` 等 audit_hints  

---

## 前置条件

- 主库四服务已启动（见 [QUICK_DEPLOY.md](https://github.com/lannisite110/web3-edu-platform-core/blob/main/docs/QUICK_DEPLOY.md)）  
- `make register-plugins PLUGINS_DIR=..` 已完成  

---

## 背景原理

`DaoVoteDemo.sol` 提供 `yesVotes` / `noVotes` mapping 与 `vote(proposalId, support)`。本平台在 **教学层** 模拟计票与 quorum，不连接真实治理代币。

---

## 分步实验

### 步骤 1：打开 Lab

浏览器访问：`http://127.0.0.1:5173/labs/edu.hot.dao`

### 步骤 2：UI 点票

1. 填写提案 ID、标题、quorum（默认 100）  
2. 点击 **投 YES +1** / **投 NO +1** 若干次  
3. 观察计票板进度条与本地计数  
4. 点击 **提交投票快照到平台**  

### 步骤 3：curl 验证

```bash
curl -s -X POST http://127.0.0.1:8080/api/v1/labs/edu.hot.dao/simulate \
  -H 'Content-Type: application/json' \
  -d '{
    "user_prompt": "DAO vote teaching",
    "params": {
      "proposal_id": "1",
      "proposal_title": "教学预算提案",
      "quorum": 100,
      "yes_votes": 55,
      "no_votes": 12
    },
    "allowed_chain_ids": [11155111]
  }' | jq '.evaluation'
```

**期望**：`compliance_passed: true`，audit_hints 含 `proposal_status=passed` 或 `active`。

### 步骤 4：自检清单

- [ ] 计票板显示 YES/NO 与 turnout  
- [ ] 任务状态变为 `completed`  
- [ ] JSON 报告可展开查看  

---

## K8s Job（可选）

Job 模板会运行 `solc` 编译 DAO 投票合约片段（见 Phase 3 toolchain gate）：

```bash
cd ../web3-edu-platform-core
make k8s-job-smoke   # 需 kubectl；busybox 回退见 DEV.md
```

---

## 相关链接

- 上一专题：[aa-session-intro.md](aa-session-intro.md)  
- 下一专题：[mev-intro.md](mev-intro.md)  
- 分阶段路线：[HOT_TOPIC_PHASES.md](../HOT_TOPIC_PHASES.md)  

---

## 合规边界

| 允许 | 禁止 |
|------|------|
| 测试网治理教学仿真 | 主网真实治理 / 代币募资 |
| 虚构提案与投票人 | 操纵真实协议治理 |

> **合规脚注**: testnet-only · 虚构数据 only
