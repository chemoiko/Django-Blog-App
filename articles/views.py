from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')       #this is to order the articles by date
    return render(request, 'articles/article_list.html', {'articles': articles})



def article_detail(request, abc):
    # return HttpResponse(abc)
    article = Article.objects.get(slug= abc)    #querying the database with that slug for a particular database that will be stored in article variable
    return render(request, 'articles/article_detail.html', {'article': article})    #send it back to a template