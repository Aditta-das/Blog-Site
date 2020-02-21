from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.cate, name='category'),
    path('<int:category_id>', views.details, name='category'),
    path('details/<int:details_id>', views.details, name='details'),
    path('details/comment/<int:details_id>', views.details, name='details'),
    path('like/', views.like_post, name='like_post'),
    path('search/', views.search, name='search'),
    path('create_post/', views.create_post, name='create_post'),
]