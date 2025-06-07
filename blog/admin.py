from django.contrib import admin
from django import forms

from .models import Article, Category

# 自定义后台表单和界面，使其支持 Markdown 编辑并更美观


class ArticleAdminForm(forms.ModelForm):
    """后台文章表单，使用 SimpleMDE 编辑 Markdown"""

    class Meta:
        model = Article
        fields = "__all__"
        widgets = {
            "content": forms.Textarea(attrs={"class": "markdown-editor"})
        }

    class Media:
        css = {
            "all": [
                "https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.css",
            ]
        }
        js = [
            "https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.js",
            "admin/js/init_markdown.js",
        ]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """文章模型的后台管理"""

    list_display = ("title", "author", "created_at", "updated_at")
    form = ArticleAdminForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
