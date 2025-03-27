from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=30, null=False)
    content = models.TextField( null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def has_comments(self):
        return self.comments.exists() if hasattr(self, 'comments') else False

    def __str__(self):
        return self.title


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Автор комментария (если авторизован)
    author_comment = models.CharField(max_length=60, default="Аноним")  # Имя анонима
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий к {self.news.title} от {self.author_comment or self.author.username}"


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Указываем уникальное имя для обратной связи
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Указываем уникальное имя для обратной связи
        blank=True
    )

    def __str__(self):
        return self.username



