from django import forms
from .models import News, Comment

from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']
    #
    # def save(self, commit=True):
    #     news = super().save(commit=False)
    #     news.author = self.request.user
    #     if commit:
    #         news.save()
    #     return news


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
