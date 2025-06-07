from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('add/', views.add_article, name='add_article'),
    path('<int:pk>/edit/', views.edit_article, name='edit_article'),
]
