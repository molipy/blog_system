# 个人博客系统

本项目基于 Django 开发，使用 Bootstrap 构建前端界面，支持 Markdown 编辑文章。

## 环境准备

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 运行数据库迁移：
   ```bash
   python manage.py migrate
   ```
3. 创建管理员账户：
   ```bash
   python manage.py createsuperuser
   ```
4. 启动开发服务器：
   ```bash
   python manage.py runserver
   ```

然后访问 `http://127.0.0.1:8000/admin/` 登录后台管理界面。

## 功能简介

- 在后台可以使用 SimpleUI 美化的界面编写和管理文章，内容支持 Markdown 格式。
- 主页提供文章列表，并通过 AJAX 实现文章的发布和编辑。
- 由于是学习项目，已关闭 CSRF 检查，切勿在线上环境使用。

