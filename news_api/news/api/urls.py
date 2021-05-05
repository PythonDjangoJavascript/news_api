from django.urls import path
from news.api import views

urlpatterns = [
    path('articles/', views.article_list_create_api_view, name='article-list'),
]
