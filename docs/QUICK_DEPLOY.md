# 快速部署 · Web3 Hot Topic Labs

> 本子库**不能单独运行**，需与主库及另外三子库同目录放置。

---

## 1. 五仓布局

```bash
mkdir -p ~/web3home && cd ~/web3home
git clone git@github.com:lannisite110/web3-edu-platform-core.git
git clone git@github.com:lannisite110/web3-hot-topic-labs.git   # 本仓
git clone git@github.com:lannisite110/supervision-trace-edu-suite.git
git clone git@github.com:lannisite110/enterprise-gov-edu-demo.git
git clone git@github.com:lannisite110/global-social-edu-sandbox.git
```

---

## 2. 注册本仓 11 插件

```bash
cd ~/web3home/web3-edu-platform-core
make register-plugins PLUGINS_DIR=..
make ci-gate
```

---

## 3. 本子库联合调试

```bash
bash ../web3-hot-topic-labs/scripts/joint-debug-smoke.sh
```

或手动启动主库四进程后访问 `/labs/edu.hot.*`。

---

## 4. K8s Job（可选）

主库目录：

```bash
make k8s-multilang-smoke   # language-advisor + evm toolchain
make k8s-job-smoke         # dao Job 模板
```

---

## 5. 更多

- 主库 [QUICK_DEPLOY.md](https://github.com/lannisite110/web3-edu-platform-core/blob/main/docs/QUICK_DEPLOY.md)
- 主库 [LEARNING_PATH.md](https://github.com/lannisite110/web3-edu-platform-core/blob/main/docs/LEARNING_PATH.md)
