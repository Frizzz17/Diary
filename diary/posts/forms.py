from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    '''Создаёт форму для нового поста.'''
    class Meta:
        model = Post

        fields = ('text', 'group')
