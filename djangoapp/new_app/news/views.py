
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serizalizers import NewsSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import View
from .models import Comment
from .models import News
from django.views.generic import ListView
from .forms import NewsForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import CreateView

# views.py
from django.shortcuts import redirect

def home(request):
    return redirect('news_list')

class NewsCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = NewsForm()
        return render(request, 'news/news_form.html', {'form': form})

    def post(self, request):
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news_detail', pk=news.pk)
        return render(request, 'news/news_form.html', {'form': form})


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
    def get(self, request, pk):
        news=get_object_or_404(News, pk=pk)
        comments=news.comments.all().order_by('-created_at')
        return render(request, 'news/news_detail.html', {'news': news, 'comments': comments})

    def post(self, request, pk):
        news=get_object_or_404(News, pk=pk)
        content=request.POST.get('content')

        if 'delete_news' in request.POST and news.author == request.user:
            news.delete()
            return redirect('news_list')
        if content:
            Comment.objects.create(news=news, content=content, author_comment=request.user.username)
            return redirect('news_detail', pk=pk)

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


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()  # Сначала сохраняем пользователя
        default_group, created = Group.objects.get_or_create(name='Обычные пользователи')
        user.groups.add(default_group)  # Добавляем пользователя в группу
        return redirect(self.success_url)


@login_required
def news_add(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news/news_form.html', {'form': form})

@login_required
def comment_add(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.user = request.user
            comment.save()
            return redirect('news_detail', pk=news_id)
    else:
        form = CommentForm()
    return render(request, 'news/comment_form.html', {'form': form, 'news': news})





class CommentAddView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name ='news/comment_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.news = get_object_or_404(News, id=self.kwargs['pk'])  # Исправляем ID
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('news_detail', kwargs={'pk': self.kwargs['pk']})


class CommentDeleteView(View):
    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if comment.author_comment == request.user.username:
            comment.delete()
        return redirect('news_detail', pk=comment.news.pk)



class NewsCreateAPIView(APIView):
    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NewsDetailAPIView(APIView):
    def get(self, request, pk):
        news_item = get_object_or_404(News, pk=pk)
        serializer = NewsSerializer(news_item)
        return Response(serializer.data)

class NewsDeleteAPIView(APIView):
    def delete(self, request, pk):
        news_item = get_object_or_404(News, pk=pk)
        news_item.delete()
        return Response({"message": "Новость удалена"}, status=status.HTTP_204_NO_CONTENT)

class NewsListAPIView(APIView):
    def get(self, request):
        news_items = News.objects.all().order_by('-created_at')
        serializer = NewsSerializer(news_items, many=True)
        return Response(serializer.data)
