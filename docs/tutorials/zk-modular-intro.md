# ZK 模块化 Rollup 教学

> **插件**: `edu.hot.zk-modular` · **TaskType**: `HOT_ZK_ROLLUP_SIM` · **Namespace**: `ns-hot-zk`

## 原理

ZK 电路与 Rollup 批次提交教学仿真（测试网 mock verifier）

## 操作步骤

1. 主库启动后端：`make run-rule-engine` / `run-scheduler` / `run-gateway`
2. 注册插件：`make register-plugins PLUGINS_DIR=..`
3. 打开 `/labs/edu.hot.zk-modular`，填写参数并提交仿真实验
4. 轮询任务状态并查看报告 JSON

## 合规边界

| 允许 | 禁止 |
|------|------|
| 测试网部署演示 | 主网上线 |
| 教学仿真与算法演示 | 生产级 Rollup / 真实交易策略 |
| 虚构数据 | 资产发行/募资/套利机器人 |

---

> **合规脚注**: testnet-only · 虚构数据 only
