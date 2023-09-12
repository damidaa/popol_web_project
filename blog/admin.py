from django.contrib import admin
from blog.models import Post,Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","thumbnail","link_url"]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass



# Register your models here.
