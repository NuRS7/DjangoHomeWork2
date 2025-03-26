from django.db import models

# Create your models here.
class News(models.Model):
    author = models.CharField(max_length=60, null=False, help_text="Автор новости", default="Автор стати")
    title = models.CharField(max_length=30, null=False)
    content = models.TextField( null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def has_comments(self):
        return self.comments.exists()  # Если related_name не указан

class Comment(models.Model):
    news = models.ForeignKey('News', on_delete=models.CASCADE,related_name='comments')
    author_comment = models.CharField(max_length=60,default="Аноним", null=True)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)


