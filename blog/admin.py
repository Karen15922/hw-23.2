from django.contrib import admin
from blog.models import Post


# ругистрация модели поста в панели администратора
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image', 'created_at', 'is_published')
