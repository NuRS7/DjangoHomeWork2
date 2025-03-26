from django.urls import path
from .views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),  # Список новостей
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('add/', NewsCreateView.as_view(), name='news_add'),
    path('<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
    # Детальная новость

# http://127.0.0.1:8000/news/add
    # http://127.0.0.1:8000/news/2/edit


    #http://127.0.0.1:8000/news/2/
]
