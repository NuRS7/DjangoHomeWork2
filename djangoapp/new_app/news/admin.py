from django.contrib import admin

# Register your models here.
# from django.contrib import admin
# from .models import News, Comment
#
#
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at')
#     search_fields = ('title', 'content')
#
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('content', 'created_at', 'news')
#     search_fields = ('content',)
#
# admin.site.register(News, NewsAdmin)
# admin.site.register(Comment, CommentAdmin)


from django.contrib import admin
from .models import News, Comment

class CommentInline(admin.TabularInline):  # Используем TabularInline для комментариев
    model = Comment
    extra = 5  # Покажет 5 пустых полей для комментариев
    readonly_fields = ('created_at',)  # Сделаем created_at только для чтения
    exclude = ('created_at',)  # Полностью исключаем его из формы

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'has_comments')  # Отображаемые поля
    inlines = [CommentInline]  # Добавляем комментарии как inline

admin.site.register(News, NewsAdmin)


