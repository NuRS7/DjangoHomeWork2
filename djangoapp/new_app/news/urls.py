from django.urls import path
from .views import NewListView, NewsDetailView

urlpatterns = [
    path('', NewListView.as_view(), name='news_list'),  # Список новостей
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),  # Детальная новость


    #http://127.0.0.1:8000/news/2/
]
