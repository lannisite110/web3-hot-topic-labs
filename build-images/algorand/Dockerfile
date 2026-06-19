# Algorand 工具链镜像：pyteal + goal/teal
# 教学用途，测试网 only
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl git build-essential ca-certificates python3 python3-pip wget \
    && rm -rf /var/lib/apt/lists/*

# pyteal (pinned)
RUN pip3 install --no-cache-dir pyteal==0.24.1

# algorand node tools (goal) for TEAL compile — testnet sandbox only
RUN wget -q https://github.com/algorand/go-algorand-sdk/releases/download/v2.6.0/linux_amd64.tar.gz \
    && tar -xzf linux_amd64.tar.gz -C /usr/local/bin goal \
    && rm linux_amd64.tar.gz \
    && chmod +x /usr/local/bin/goal || true

WORKDIR /workspace
ENV EDU_LANG_GROUP=algorand
ENTRYPOINT ["bash", "-c", "echo '==> Algorand (TEAL) toolchain ready (testnet-only)' && exec \"$@\"", "--"]
