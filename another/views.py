from django.http import HttpResponse
from django.contrib import admin
from django.shortcuts import render     #this is to render stuff




def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def article_create(request):
    return render(request, 'articles/article_create.html')