from django.urls import path
from . import views

urlpatterns = [
  path('', views.apiOverview, name='api-overview'),
  path('news-list/', views.newList, name='news-list'),
  path('detail-new/<str:pk>/', views.newDetail, name='detail-new'),
  path('news-create/', views.newCreate, name='news-create'),
  path('news-update/<str:pk>/', views.newUpdate, name='news-update'),
  path('news-delete/<str:pk>/', views.newDelete, name='news-delete'),
  path('news-comments/', views.commentList, name='news-comments'),
  path('comment-create/', views.commentCreate, name='comment-create')

]