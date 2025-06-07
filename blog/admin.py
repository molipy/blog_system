from django.contrib import admin

from .models import Article, Category

# 在后台管理中注册模型，便于管理文章和类别


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "updated_at")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
