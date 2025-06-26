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
    apt-get install -y --no-install-recommends \
    postgresql-server-dev-all \
    gcc \
    g++ \
    make \
    libsass-dev \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    musl-dev \
    wget  \
    curl

# 安装字体依赖
RUN apt-get install -y --no-install-recommends \
    ca-certificates \
    libx11-6 \
    libxcb1 \
    libxext6 \
    libxrender1 \
    libjpeg62-turbo \
    fonts-wqy-zenhei \
    fonts-wqy-microhei \
    xfonts-75dpi \
    xfonts-base \
    ttf-wqy-zenhei \
    ttf-wqy-microhei \
    fontconfig && \
    fc-cache -f



# 安装wkhtmltopdf
COPY ./wkhtmltox_0.12.6.1-3.bookworm_amd64.deb ./wkhtmltox.deb
RUN dpkg -i ./wkhtmltox.deb || true && \
    apt-get install -f -y --no-install-recommends && \
    rm -rf ./wkhtmltox.deb

# 验证
RUN wkhtmltopdf --version && \
    echo "Installation verified."

# 清理
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 创建插件目录
RUN mkdir -p $ADDONSDIR

# 创建odoo用户和用户组
RUN groupadd -g 1000 odoo && \
    useradd -u 1000 -g odoo -d $WORKDIR -s /bin/bash odoo && \
    mkdir -p $WORKDIR && \
    chown odoo:odoo $WORKDIR

COPY ./odoo-16.0.20250606-py3-none-any.whl $ODOO_PACKAGE
COPY ./addons $ADDONSDIR

# 修正文件权限
RUN chown -R odoo:odoo $WORKDIR && \
    chmod -R 755 $WORKDIR

# 安装python相关依赖包
RUN pip install --use-pep517 --no-build-isolation --root-user-action=ignore -U pip -i https://mirrors.huaweicloud.com/repository/pypi/simple && \
    pip install --use-pep517 --no-build-isolation --root-user-action=ignore $ODOO_PACKAGE && \
    pip install --use-pep517 --no-build-isolation --root-user-action=ignore Werkzeug==1.0.1 -i https://mirrors.huaweicloud.com/repository/pypi/simple && \
    pip install --use-pep517 --no-build-isolation --root-user-action=ignore inotify==0.2.10 -i https://mirrors.huaweicloud.com/repository/pypi/simple && \
    rm -rf /root/.cache/pip

# 切换到odoo用户运行
USER odoo
WORKDIR $WORKDIR