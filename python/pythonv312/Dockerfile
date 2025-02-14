# 使用 Python 3.12.7 Alpine 作为基础镜像
FROM python:3.12.7-alpine

# 设置维护者信息
LABEL maintainer="ckf10000@sina.com"

###############################################################################
# 安装所需依赖
###############################################################################

# 更新 apk 包索引并安装依赖工具
RUN apk update && \
    apk add --no-cache gcc g++ libffi-dev openssl-dev libxml2-dev libxslt-dev build-base musl-dev wget curl && \
    # 升级 pip 到最新版
    pip install --root-user-action=ignore -U pip
