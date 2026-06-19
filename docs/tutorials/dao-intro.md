# DAO 投票教学

> **插件**: `edu.hot.dao` · **TaskType**: `HOT_DAO_VOTE_SIM` · **Namespace**: `ns-hot-sim`

## 原理

测试网 DAO 提案与投票计数教学

## 操作步骤

1. 主库启动后端：`make run-rule-engine` / `run-scheduler` / `run-gateway`
2. 注册插件：`make register-plugins PLUGINS_DIR=..`
3. 打开 `/labs/edu.hot.dao`，填写参数并提交仿真实验
4. 轮询任务状态并查看报告 JSON

## 合规边界

| 允许 | 禁止 |
|------|------|
| 测试网部署演示 | 主网上线 |
| 教学仿真与算法演示 | 生产级 Rollup / 真实交易策略 |
| 虚构数据 | 资产发行/募资/套利机器人 |
