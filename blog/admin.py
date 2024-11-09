from django.contrib import admin

# Register your models here.
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')

admin.site.register(Post, PostAdmin)