# BTC L2 工具链镜像：clarity CLI
# 教学用途，测试网 only
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl git build-essential ca-certificates nodejs npm \
    && rm -rf /var/lib/apt/lists/*

# clarinet (Stacks Clarity toolchain, pinned)
RUN npm install -g @stacks/clarinet@2.9.0

WORKDIR /workspace
ENV EDU_LANG_GROUP=btc
ENTRYPOINT ["bash", "-c", "echo '==> BTC L2 (Clarity) toolchain ready (testnet-only)' && exec \"$@\"", "--"]
