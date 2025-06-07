from django.db import models
from django.contrib.auth.models import User
import html

try:
    import markdown as md_lib
except Exception:  # pragma: no cover - fallback if markdown not installed
    md_lib = None

# 模型定义：文章和类别


class Category(models.Model):
    """文章类别模型"""
    name = models.CharField("名称", max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    """文章模型"""

    title = models.CharField("标题", max_length=200)
    content = models.TextField("内容")
    category = models.ForeignKey(
        Category, verbose_name="类别", on_delete=models.SET_NULL, null=True, blank=True
    )
    author = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return self.title

    def content_as_html(self):
        """将 Markdown 内容渲染为 HTML"""
        if md_lib:
            return md_lib.markdown(self.content)
        # 简单降级处理：转义后换行转换为 <br>
        return "<br>".join(html.escape(line) for line in self.content.splitlines())

