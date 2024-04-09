from multiprocessing import context
from django.shortcuts import render
from .models import News  

def news(request):
     news_list = News.objects.order_by('-date')
     context = {'news_list': news_list}
     return render(request, 'news.html', context)
