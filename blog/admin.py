from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created','publish','status','author')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title','body','slug')
    ordering = ('author','publish','status')
    list_filter = ('author','created','publish')