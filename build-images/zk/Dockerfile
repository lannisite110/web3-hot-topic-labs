# ZK 工具链镜像：cairo + starknet-foundry
# 教学用途，测试网 only
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl git build-essential ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# scarb + starknet-foundry (pinned installer)
RUN curl -fsSL https://docs.starknet.io/scripts/install.sh | sh -s -- --yes
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /workspace
ENV EDU_LANG_GROUP=zk
ENTRYPOINT ["bash", "-c", "echo '==> ZK toolchain ready (testnet-only)' && exec \"$@\"", "--"]
