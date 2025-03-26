from django.test import TestCase
from django.urls import reverse
from .models import News, Comment

class NewsViewsTest(TestCase):

    def setUp(self):
        self.news1 = News.objects.create(title="Старая новость", author="Автор1", content="Контент 1")
        self.news2 = News.objects.create(title="Новая новость", author="Автор2", content="Контент 2")

        self.comment1 = Comment.objects.create(news=self.news2, content="Первый комментарий", author_comment="User1")
        self.comment2 = Comment.objects.create(news=self.news2, content="Второй комментарий", author_comment="User2")

    def test_news_list_sorted_by_created_at_desc(self):
        response = self.client.get(reverse('news_list'))
        self.assertEqual(response.status_code, 200)
        news_list = response.context['news']
        self.assertGreaterEqual(news_list[0].created_at, news_list[1].created_at)

    def test_news_detail_view(self):

        response = self.client.get(reverse('news_detail', args=[self.news2.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.news2.title)
        self.assertContains(response, self.news2.content)

    def test_news_detail_with_comments_sorted(self):
        response = self.client.get(reverse('news_detail', args=[self.news2.id]))
        self.assertEqual(response.status_code, 200)
        comments = response.context['comments']
        self.assertGreaterEqual(comments[0].created_at, comments[1].created_at)
