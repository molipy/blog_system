from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render

from .forms import ArticleForm
from .models import Article

# 以下视图函数通过 AJAX 提供文章的增删改查操作

# 视图函数，提供文章的增删改查接口


def article_list(request):
    """文章列表视图"""


    # 获取所有文章，按创建时间倒序排列
    articles = Article.objects.all().order_by("-created_at")
    # 页面上用于新增文章的表单
    form = ArticleForm()
    return render(request, "blog/article_list.html", {"articles": articles, "form": form})


@login_required
def add_article(request):
    if request.method == "POST":
        # 提交表单保存文章
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return JsonResponse({
                "id": article.id,
                "title": article.title,
                "content": article.content_as_html(),
                "markdown": article.content,
                "author": article.author.username,
                "category": article.category.name if article.category else "",
                "created_at": article.created_at.strftime("%Y-%m-%d %H:%M"),
            })
        return JsonResponse({"errors": form.errors}, status=400)
    return HttpResponseBadRequest("Invalid request")


@login_required
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user)
    if request.method == "POST":
        # 更新现有文章
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return JsonResponse({
                "id": article.id,
                "title": article.title,
                "content": article.content_as_html(),
                "markdown": article.content,
                "category": article.category.name if article.category else "",
            })
        return JsonResponse({"errors": form.errors}, status=400)
    return HttpResponseBadRequest("Invalid request")

