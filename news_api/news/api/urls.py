from django.urls import path
from news.api import views

urlpatterns = [
    path('articles/', views.article_list_create_api_view, name='article-list'),
    path('articles/<int:pk>/', views.article_detail_api_view, name='article-detail'),
    path('articlescls/', views.ArticleListApiView.as_view(), name='articlecls-list'),
    path('articlescls/<int:pk>/', views.ArticleDetailApiView.as_view(),
         name='articlecls-detail'),
    path('journalist/', views.JournalistApiView.as_view(), name='journalist-list'),
    path('journalist/<int:id>/', views.JournalistDetailApiView.as_view(),
         name='journalist-detail'),
]
