from django import forms
from .models import Article,Comment


class ArticleForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    body=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model=Article
        fields=('title','body','is_public')


class CommentForm(forms.ModelForm):
    comment=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model=Comment
        fields=('article','comment')

    def __init__(self, article_id=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if article_id:
            self.fields['article'].initial=article_id
