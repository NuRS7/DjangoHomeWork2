from django.urls import path
from .views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView, CommentDeleteView
from .views import news_add, CommentAddView
urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),  # Список новостей
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('add/', NewsCreateView.as_view(), name='news_add'),
    path('<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
    path('news/add/', news_add, name='news_add'),
    path('news/<int:news_id>/comment/', CommentAddView.as_view(), name='comment_add'),
    path('news/<int:pk>/delete/', NewsDetailView.as_view(), name='news_delete'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),


    # Детальная новость

# http://127.0.0.1:8000/news/add
    # http://127.0.0.1:8000/news/2/edit


    #http://127.0.0.1:8000/news/2/
]
