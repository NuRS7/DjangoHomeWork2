from django.urls import path
from .views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView, CommentDeleteView, NewsListAPIView, \
    NewsDetailAPIView, NewsDeleteAPIView
from .views import news_add, CommentAddView
from .views import NewsCreateAPIView
urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),  # Список новостей
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('add/', NewsCreateView.as_view(), name='news_add'),
    path('<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
    path('news/add/', news_add, name='news_add'),
    path('news/<int:news_id>/comment/', CommentAddView.as_view(), name='comment_add'),
    path('news/<int:pk>/delete/', NewsDetailView.as_view(), name='news_delete'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('api/news/', NewsListAPIView.as_view(), name='news_list_api'),
    path('api/news/<int:pk>/', NewsDetailAPIView.as_view(), name='news_detail_api'),
    path('api/news/<int:pk>/delete/', NewsDeleteAPIView.as_view(), name='news_delete_api'),
    path('api/news/add/', NewsCreateAPIView.as_view(), name='news_create_api'),


    # Детальная новость

# http://127.0.0.1:8000/news/add
    # http://127.0.0.1:8000/news/2/edit


    #http://127.0.0.1:8000/news/2/
]
