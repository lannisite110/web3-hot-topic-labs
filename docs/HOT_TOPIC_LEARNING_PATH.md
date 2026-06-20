# Web3 热点专题 · 完整学习路径

> **子库** `web3-hot-topic-labs` v0.4.0 · 主库 ≥ v1.1.0 · **11 插件**  
> 交叉引用：主库 [LEARNING_PATH.md](../web3-edu-platform-core/docs/LEARNING_PATH.md) **阶段 3A**

---

## 路线总览（约 2 周业余 / 1 周全职）

```text
language-advisor（入口）
    ├─→ zk-modular → zk-circuit
    ├─→ aa-wallet → aa-session
    ├─→ dao → mev
    └─→ did → depin / rwa-edu / ai-agent
```

---

## 第 0 步：环境与注册（所有 Lab 共用）

```bash
cd ~/web3home/web3-edu-platform-core
make register-plugins PLUGINS_DIR=..
make run-rule-engine & make run-scheduler & make run-gateway &
cd frontend-web && npm run dev
# → http://127.0.0.1:5173
```

详见主库 [QUICK_DEPLOY.md](https://github.com/lannisite110/web3-edu-platform-core/blob/main/docs/QUICK_DEPLOY.md)。

---

## 第 1 步：语言择优入口（必做）

| 项 | 内容 |
|----|------|
| 插件 | `edu.hot.language-advisor` |
| 教程 | [tutorials/language-advisor-intro.md](tutorials/language-advisor-intro.md) |
| UI | 9 场景 chip → 推荐卡片 → 跳转专题 Lab |
| 进阶 | `task_type: HOT_MULTI_LANG_COMPILE` 编译 Job |

**自检**：选「ZK Rollup」→ 推荐 Cairo → 能打开 `edu.hot.zk-modular`。

---

## 第 2 步：ZK 专题（2–3 天）

| 顺序 | 插件 | 教程 | 重点 |
|------|------|------|------|
| 2.1 | `edu.hot.zk-modular` | [zk-modular-intro.md](tutorials/zk-modular-intro.md) | Rollup 流水线、mock batch root |
| 2.2 | `edu.hot.zk-circuit` | [zk-circuit-intro.md](tutorials/zk-circuit-intro.md) | Cairo 电路、scarb Job |

**K8s**：`k8s/overlays/ns-hot-zk/` · `make k8s-job-smoke`（可选）

---

## 第 3 步：账户抽象 AA（1–2 天）

| 顺序 | 插件 | 教程 | 重点 |
|------|------|------|------|
| 3.1 | `edu.hot.aa-wallet` | [aa-wallet-intro.md](tutorials/aa-wallet-intro.md) | 4337 五步 UserOp 流程 |
| 3.2 | `edu.hot.aa-session` | [aa-session-intro.md](tutorials/aa-session-intro.md) | 会话密钥 TTL |

---

## 第 4 步：治理与 MEV（1–2 天）

| 顺序 | 插件 | 教程 | 重点 |
|------|------|------|------|
| 4.1 | `edu.hot.dao` | [dao-intro.md](tutorials/dao-intro.md) | 本地点票 + quorum + Job solc 编译 |
| 4.2 | `edu.hot.mev` | [mev-intro.md](tutorials/mev-intro.md) | PBS 拍卖、禁止套利机器人 |

---

## 第 5 步：身份与基础设施仿真（1–2 天）

| 顺序 | 插件 | 教程 | 重点 |
|------|------|------|------|
| 5.1 | `edu.hot.did` | [did-intro.md](tutorials/did-intro.md) | 选择性披露、Move toolchain |
| 5.2 | `edu.hot.depin` | [depin-intro.md](tutorials/depin-intro.md) | Solana Anchor 节点仿真 |
| 5.3 | `edu.hot.rwa-edu` | [rwa-edu-intro.md](tutorials/rwa-edu-intro.md) | 虚构 RWA 映射（非募资） |
| 5.4 | `edu.hot.ai-agent` | [ai-agent-intro.md](tutorials/ai-agent-intro.md) | Agent 权限边界沙箱 |

---

## 教程索引

完整列表见 [tutorials/README.md](tutorials/README.md)。

---

## 工程化验收

```bash
cd ../web3-edu-platform-core
make tutorial-audit PLUGINS_DIR=..
make integration-all-plugins   # 含 11 热点 + mock
make k8s-job-smoke             # 可选，需 K8s
```

分阶段路线图：[HOT_TOPIC_PHASES.md](HOT_TOPIC_PHASES.md)（Phase 0–4 已完成）。

---

## 合规提醒

测试网 / 沙箱 only · 禁止主网 · 禁止 ICO/套利/真实 RWA — [COMPLIANCE_MASTER.md](../../COMPLIANCE_MASTER.md)
