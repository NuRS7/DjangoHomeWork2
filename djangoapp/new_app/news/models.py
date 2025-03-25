from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    news = models.ForeignKey('News', on_delete=models.CASCADE,related_name='comments')
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

