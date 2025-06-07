from django.urls import path
from . import views

# 应用的 URL 路由配置

app_name = "blog"
urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('add/', views.add_article, name='add_article'),
    path('<int:pk>/edit/', views.edit_article, name='edit_article'),
]
