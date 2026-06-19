# Flow 工具链镜像：cadence / flow CLI
# 教学用途，测试网 only
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl git build-essential ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Flow CLI (pinned)
RUN sh -ci "$(curl -fsSL https://storage.googleapis.com/flow-cli/install.sh)" v1.14.2

WORKDIR /workspace
ENV EDU_LANG_GROUP=flow
ENTRYPOINT ["bash", "-c", "echo '==> Flow (Cadence) toolchain ready (testnet-only)' && exec \"$@\"", "--"]
