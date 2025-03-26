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

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5
    readonly_fields = ('created_at',)
    exclude = ('created_at',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'has_comments')
    inlines = [CommentInline]
admin.site.register(News, NewsAdmin)


