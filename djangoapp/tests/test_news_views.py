import pytest
from django.urls import reverse
from djangoapp.new_app.news.models import News, Comment

@pytest.fixture
def create_news(db):
    """Фикстура для создания новостей"""
    news1 = News.objects.create(author="Author 1", title="Title 1", content="Content 1")
    news2 = News.objects.create(author="Author 2", title="Title 2", content="Content 2")
    return [news2, news1]  # Должны быть отсортированы по убыванию created_at

@pytest.fixture
def create_comments(db, create_news):
    """Фикстура для создания комментариев к новости с id=102"""
    news = News.objects.create(id=102, author="Author 102", title="Title 102", content="Content 102")
    comment1 = Comment.objects.create(news=news, author_comment="User1", content="Comment 1")
    comment2 = Comment.objects.create(news=news, author_comment="User2", content="Comment 2")
    return [comment2, comment1]  # Должны быть отсортированы по убыванию created_at

@pytest.mark.django_db
def test_news_list_view(client, create_news):
    """Проверяет, что главная страница возвращает новости в порядке убывания"""
    response = client.get(reverse('news-list'))  # Замените 'news-list' на ваш URL name
    assert response.status_code == 200
    data = response.json()  # Если API возвращает JSON
    assert data[0]['title'] == "Title 2"
    assert data[1]['title'] == "Title 1"

@pytest.mark.django_db
def test_news_detail_view(client, create_comments):
    """Проверяет, что маршрут '102/' возвращает детали новости"""
    response = client.get(reverse('news-detail', args=[102]))  # Замените 'news-detail' на ваш URL name
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == "Title 102"
    assert data['content'] == "Content 102"

@pytest.mark.django_db
def test_news_comments_sorted(client, create_comments):
    """Проверяет, что комментарии к новости 102 отсортированы по убыванию"""
    response = client.get(reverse('news-comments', args=[102]))  # Замените 'news-comments' на ваш URL name
    assert response.status_code == 200
    data = response.json()
    assert data[0]['content'] == "Comment 2"
    assert data[1]['content'] == "Comment 1"
