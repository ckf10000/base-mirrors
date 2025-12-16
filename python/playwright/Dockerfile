# 使用 Python 3.12.9 slim 作为基础镜像
FROM swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/python:3.12.9-slim
# 设置维护者信息
LABEL maintainer="ckf10000@sina.com"

# --------------------------------------------------------
# 1. 安装 chromium 和 Playwright 所需系统依赖
# --------------------------------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    wget \
    git \
    ffmpeg \
    xvfb \
    libnss3 \
    libffi-dev \
    libxkbcommon0 \
    libasound2 \
    libatk1.0-0 \
    libcups2 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libxshmfence1 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxcursor1 \
    libxss1 \
    libxml2-dev \
    libxtst6 \
    libxslt-dev \
    ca-certificates \
    fonts-liberation \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# --------------------------------------------------------
# 2. 安装 Playwright 和 Chromium
# --------------------------------------------------------
RUN pip install --no-cache-dir playwright -i https://mirrors.huaweicloud.com/repository/pypi/simple &&  \
    # 升级 pip 到最新版
    pip install --no-cache-dir -U pip  -i https://mirrors.huaweicloud.com/repository/pypi/simple && \
    pip install --no-cache-dir -U playwright-stealth  -i https://mirrors.huaweicloud.com/repository/pypi/simple && \
    playwright install chromium