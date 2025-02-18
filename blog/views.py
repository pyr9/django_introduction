from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from blog.models import Article


def hello_world(request):
    return HttpResponse("Hello, world. This is first page.")

def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    content = article.content
    id = article.id
    pub_date = article.pub_date
    return_str = 'id: %s, title: %s, content: %s, pub_date: %s' % (id, title, content, pub_date)
    return HttpResponse(return_str)