from django.urls import path
from . import views
from blog.views import blog_list

urlpatterns = [
    path('', views.index, name='index'),  # Set the index view as the home page
    path('', blog_list, name='blog_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/new/', views.article_create, name='article_create'),
    path('article/<int:pk>/edit/', views.article_update, name='article_update'),
    path('article/<int:pk>/delete/', views.article_delete, name='article_delete'),
]

