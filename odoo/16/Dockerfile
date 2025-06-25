# 使用 Python 3.9 slim 作为基础镜像
FROM swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/python:3.9-slim

# 设置维护者信息
LABEL maintainer="ckf10000@sina.com"

###############################################################################
# 安装所需依赖
###############################################################################
# 设置工作目录路径
ENV WORKDIR=/opt/odoo
ENV ADDONSDIR=$WORKDIR/addons
ENV ODOO_PACKAGE=$WORKDIR/odoo-16.0.20250606-py3-none-any.whl

# 更新 apt 包索引并安装依赖工具
RUN apt-get update && \
    apt-get install -y postgresql-server-dev-all gcc g++ make libsass-dev libffi-dev libxml2-dev libxslt-dev musl-dev wget curl && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p $ADDONSDIR

COPY ./odoo-16.0.20250606-py3-none-any.whl $ODOO_PACKAGE
COPY ./addons $ADDONSDIR

# 安装python相关依赖包
RUN pip install --root-user-action=ignore -U pip -i https://mirrors.huaweicloud.com/repository/pypi/simple && \
    pip install --use-pep517 --no-build-isolation --root-user-action=ignore $ODOO_PACKAGE && \
    pip install Werkzeug==1.0.1 && \
    rm -rf /root/.cache/pip
