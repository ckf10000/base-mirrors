# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  cronjob-1717
# FileName:     app.py
# Description:  执行器的入口
# Author:       ASUS
# CreateDate:   2025/11/24
# Copyright ©2011-2025. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import os
import sys
import importlib
import threading
from watchdog.observers import Observer
from pyxxl import ExecutorConfig, PyxxlRunner
from watchdog.events import FileSystemEventHandler

jobs_path = "jobs"

# ---------------------------------------------------
# 1. 配置 Pyxxl 执行器（官方规范）
# ---------------------------------------------------
config = ExecutorConfig(
    xxl_admin_baseurl=os.getenv("XXL_JOB_ADMIN_ADDRESS", "http://192.168.3.240:18070/xxl-job-admin/api/"),
    executor_app_name=os.getenv("XXL_JOB_EXECUTOR_APPNAME", "python-executor-local"),

    # 官方推荐字段名称
    executor_listen_host="0.0.0.0",
    executor_listen_port=int(os.getenv("XXL_JOB_EXECUTOR_PORT", 9999)),

    # 这里指定 Admin 可访问的地址（必须是真实 IP + 端口 或域名）
    executor_url=os.getenv("XXL_JOB_EXECUTOR_URL", "http://192.168.3.86:9999/"),
    # 执行器绑定的http服务的url,xxl-admin通过这个host来回调pyxxl执行器.
    # Default: "http://{executor_listen_host}:{executor_listen_port}"

    access_token=os.getenv("XXL_JOB_ACCESS_TOKEN", "Abc123456"),
    executor_log_path="./logs/python-executor.log",

    # 建议开启 debug，便于定位注册成功与否
    debug=True,
)

executor = PyxxlRunner(config)


# ---------------------------------------------------
# 2. 通用加载任务函数
# ---------------------------------------------------
def load_job_module(module_path):
    """通用加载任务模块并注册的函数"""
    try:
        module = importlib.import_module(module_path)

        if hasattr(module, "register"):
            module.register(executor)
            print(f"[pyxxl] 加载任务: {module_path}")
        else:
            print(f"[pyxxl] {module_path} 未定义 register(executor)，跳过")

    except Exception as e:
        print(f"[pyxxl] 加载任务 {module_path} 失败: {e}")


# ---------------------------------------------------
# 2. 自动扫描 jobs/ 目录并调用 register(executor)
# ---------------------------------------------------
def auto_load_jobs():
    if not os.path.exists(jobs_path):
        print("[pyxxl] jobs 目录不存在，跳过加载")
        return

    for filename in os.listdir(jobs_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            module_path = f"{jobs_path}.{module_name}"

            # 调用通用加载任务函数
            load_job_module(module_path)


# ---------------------------------------------------
# 4. 使用 watchdog 动态监控目录变化并重新加载任务
# ---------------------------------------------------
class JobFileEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"[watchdog] 检测目录<{jobs_path}>文件状态中....")
        # 只在 `.py` 文件被修改时重新加载任务
        if event.src_path.endswith(".py") and not event.src_path.endswith("__init__.py"):
            print(f"[watchdog] 文件已修改: {event.src_path}")
            module_name = os.path.basename(event.src_path)[:-3]
            module_path = f"{jobs_path}.{module_name}"

            # 卸载并重新加载模块
            if module_name in sys.modules:
                del sys.modules[module_path]

            # 调用通用加载任务函数
            load_job_module(module_path)


def start_job_watchdog():
    event_handler = JobFileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, jobs_path, recursive=False)
    observer.start()
    print(f"[watchdog] 开始监控 {jobs_path} 目录变化...")
    try:
        observer.join()  # 直接等待 observer 线程结束
    except KeyboardInterrupt:
        observer.stop()  # 捕获 Ctrl+C 停止监控
        observer.join()  # 确保 monitor 线程正确结束


# ---------------------------------------------------
# 5. 启动 Pyxxl 执行器并启动监控
# ---------------------------------------------------
if __name__ == "__main__":
    # 首先加载一次任务
    print("[pyxxl] 扫描并加载 jobs 目录中的任务...")
    auto_load_jobs()

    # 启动 watchdog 监控文件变化的线程
    # start_job_watchdog()
    watchdog_thread = threading.Thread(target=start_job_watchdog, daemon=True)
    watchdog_thread.start()

    # 启动执行器
    print("[pyxxl] 启动 XXL-JOB Python 执行器...")
    executor.run_executor()
