from django.apps import AppConfig


# 应用配置类，Django 会自动读取此配置
class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
