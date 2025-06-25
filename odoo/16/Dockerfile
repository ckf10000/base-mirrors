# 使用 Python 3.11.9 Alpine 作为基础镜像
FROM swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/python:3.9-slim

# 设置维护者信息
LABEL maintainer="ckf10000@sina.com"

###############################################################################
# 安装所需依赖
###############################################################################
# 设置工作目录路径
ENV WORKDIR=/tmp

COPY ./odoo-16.0.20250606-py3-none-any.whl $WORKDIR

# 更新 apk 包索引并安装依赖工具
RUN apt-get update && \
    apt-get install -y postgresql-server-dev-all gcc g++ make libsass-dev libffi-dev libxml2-dev libxslt-dev musl-dev wget curl && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --root-user-action=ignore -U pip -i https://mirrors.huaweicloud.com/repository/pypi/simple && \
    pip install --use-pep517 --no-build-isolation --root-user-action=ignore $WORKDIR/odoo-16.0.20250606-py3-none-any.whl && \
    pip install Werkzeug==1.0.1 && \
    rm -rf /root/.cache/pip
