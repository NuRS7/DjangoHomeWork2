
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import View
from .models import News, Comment


class NewListView(View):
    def get(self, request):
        news = News.objects.all().order_by('-created_at')
        return render(request, 'news/news_list.html', {'news': news})

class NewsDetailView(View):
    def get(self,request,pk):
        news = get_object_or_404(News,pk=pk)
        comment = news.comments.all().order_by('-created_at')
        return render(request, 'news/news_detail.html',{'news': news, 'comments': comment})
    def post(self, request, pk):
        news = get_object_or_404(News, pk=pk)
        content =request.POST.get('content')

        if content:
            Comment.objects.create(news=news, content=content)

        return redirect('news_detail', pk=pk)


