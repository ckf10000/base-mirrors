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


OCR构建
- docker buildx build -f ./Dockerfile -t ocr-python312:20251126 .