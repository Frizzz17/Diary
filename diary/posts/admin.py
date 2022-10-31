from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'author')

admin.site.register(Post)