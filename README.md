# base-mirrors
基础镜像

# 构建

odoo构建
- docker build -f ./Dockerfile -t my-odoo:16.20250626 .
或者新版本docker
- docker buildx build -f ./Dockerfile -t my-odoo:16.20250626 .

python构建
- docker build -f ./Dockerfile -t my-python311:20250626 .
- docker build -f ./Dockerfile -t my-python312:20250626 .
或者新版本docker
- docker buildx build -f ./Dockerfile -t my-python311:20250626 .
- docker buildx build -f ./Dockerfile -t my-python312:20250626 .


playwright构建
- docker buildx build -f ./Dockerfile -t my-python3.12.9-slim:latest .

xxl-job-python-executor构建
- docker buildx build -f ./Dockerfile -t xxl-job-executor-python:latest .

xxl-job-java-executor构建
- docker buildx build -f ./Dockerfile -t xxl-job-executor-java:latest .