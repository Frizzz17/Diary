from django.contrib import admin
from .models import Post, Group

class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'author', 'group')


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
