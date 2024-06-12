from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')       #this is to order the articles by date
    return render(request, 'articles/article_list.html', {'articles': articles})



def article_detail(request, abc):
    # return HttpResponse(abc)
    article = Article.objects.get(slug= abc)    #querying the database with that slug for a particular database that will be stored in article variable
    return render(request, 'articles/article_detail.html', {'article': article})    #send it back to a template


@login_required(login_url="/accounts/login/")       #this is a decorator protecting this view from anyone who hasnt logged in and anyone who is not logged in will be redirected to that url
def article_create(request):
    if request.method =='POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            #save article to db
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form':form})    #send it back to a template


