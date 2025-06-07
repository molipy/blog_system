from django import forms
from .models import Article, Category

# 表单定义，供前端提交使用



class ArticleForm(forms.ModelForm):
    """文章表单"""

    class Meta:
        model = Article
        # 需要在表单中呈现的字段
        fields = ["title", "content", "category"]
