
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import View
from .models import News, Comment
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import News
from django.views.generic import ListView, DetailView, UpdateView
from .forms import NewsForm



# views.py
from django.shortcuts import redirect

def home(request):
    return redirect('news_list')

class NewsCreateView(CreateView):
    model = News
    fields = ['title', 'content']
    template_name = 'news/news_form.html'
    success_url = reverse_lazy('news_list')

# class NewsCreateView(View):
#     def get(self, request):
#         form = NewsForm()
#         return render(request, 'news/news_form.html', {'form': form})
#     def post(self,request):
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('news_list')
#         return render(request, 'news/news_form.html', {'form': form})


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'  # Создайте этот шаблон для отображения списка новостей
    context_object_name = 'news_list'

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

class NewsUpdateView(View):
    def get(self, request, pk):
        news_item = get_object_or_404(News, pk=pk)
        form = NewsForm(instance=news_item)
        return render(request, 'news/news_form.html', {'form': form})

    def post(self, request, pk):
        news_item = get_object_or_404(News, pk=pk)
        form = NewsForm(request.POST, instance=news_item)
        if form.is_valid():
            form.save()  # сохраняем обновления новости
            return redirect('news_detail', pk=news_item.pk)  # перенаправляем на страницу новости
        return render(request, 'news/news_form.html', {'form': form})

# class NewsDetailView(DetailView):
#     model = News
#     template_name = 'news/news_detail.html'
#     context_object_name = 'news'

    def get_success_url(self):
        return redirect('news_detail', pk=self.object.pk)