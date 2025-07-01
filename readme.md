# STPlatform 启动说明

本项目基于 [Poetry](https://python-poetry.org/) 进行依赖管理，后端框架为 Django。

---

## 快速启动

以下是开发环境下的启动流程：

```bash
# 1. 安装依赖（首次）
poetry install

# 2. 创建 Django 项目（首次，若项目已存在可跳过）
poetry run django-admin startproject STPlatform

# 3. 启动开发服务器
分开跑 不共享内存
poetry run python manage.py runserver 8080
poetry run daphne STPlatform.asgi:application -b 0.0.0.0 -p 20080
一起跑 共享内存(建议)
poetry run daphne STPlatform.asgi:application -b 0.0.0.0 -p 8000


```
## poetry 常用命令参考
```bash
poetry install	 #安装依赖
poetry add <package>	#添加依赖包
poetry run <command>	#执行命令
```

## grations 常用命令参考
```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```




