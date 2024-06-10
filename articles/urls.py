from django.urls import path
from . import views

app_name = 'articles'   #this is called namespacing to not confuse the urls of multiple apps e.g name = 'detail' could also be in another app called office so it would finally be called articles:detail
urlpatterns = [
   
    path('', views.article_list),
    path('<slug:abc>/', views.article_detail, name='detail'),
]