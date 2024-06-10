from django.urls import path
from . import views


urlpatterns = [
   
    path('', views.article_list),
    path('<slug:abc>/', views.article_detail, name='article_detail'),
]