from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import News, Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'news')
    search_fields = ('content',)

admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
