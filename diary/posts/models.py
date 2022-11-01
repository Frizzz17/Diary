from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Group(models.Model):
    '''Создает группу.'''
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.title[:15]


class Post(models.Model):
    '''Создаёт объект поста.'''
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts'
    )

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.text[:15]
