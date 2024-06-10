from django.db import models

# Create your models here.
#this will all be transformed into a table in the database with title,slug,body.date as the columns
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug =  models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank=True)

    #this below is a method which obviously should be within a class
    def __str__(self):      #this will help us to show the title of the object when we run Article.objects.all() instead of just showing us cryptic things like <Article: Article object(1)>
        return self.title
    

    def snippet(self):      #this shows first 50 characters of the article
        return self.body[:50] + '...'