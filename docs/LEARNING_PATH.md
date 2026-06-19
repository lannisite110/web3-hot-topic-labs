# 学习路径 · Web3 Hot Topic Labs（子库1）

> **本仓** v0.3.0 · 主库 [web3-edu-platform-core](https://github.com/lannisite110/web3-edu-platform-core) **v1.0.0**  
> 11 个热点教学插件 + 多语言 toolchain 镜像定义。

---

## 阅读顺序

| 顺序 | 路径 | 目的 |
|------|------|------|
| 1 | 主库 `docs/PLUGIN_CONTRACT.md` | 插件契约（必读） |
| 2 | [TASK.md](../TASK.md) | 本子库任务书 |
| 3 | [docs/multi-language-toolchains.md](multi-language-toolchains.md) | 七组镜像与 Namespace |
| 4 | `plugins/*/plugin.manifest.yaml` | 各插件 TaskType / jobTemplate |
| 5 | `plugins/*/docs/tutorials/*.md` | 实验教程 |

全平台路径见主库 [docs/LEARNING_PATH.md](https://github.com/lannisite110/web3-edu-platform-core/blob/main/docs/LEARNING_PATH.md)。

---

## 推荐插件实验顺序

1. `edu.hot.language-advisor` — 语言择优 + `HOT_MULTI_LANG_COMPILE`
2. `edu.hot.dao` — DAO 投票仿真（K8s Job 模板）
3. `edu.hot.zk-circuit` — ZK 电路编译
4. `edu.hot.aa-wallet` — 账户抽象
5. `edu.hot.mev` — MEV PBS 仿真
6. 其余热点 Lab 按侧边栏浏览

---

## 本仓独有内容

- `build-images/manifest.yaml` — toolchain 镜像组（container-manager 读取）
- `k8s/overlays/*/` — 各插件 Job 模板
- `scripts/generate-labs.py` — 批量脚手架

---

## 合规

测试网/仿真 only · 禁止主网 · [COMPLIANCE_MASTER.md](https://github.com/lannisite110/web3-edu-platform-core/blob/main/docs/COMPLIANCE.md)
