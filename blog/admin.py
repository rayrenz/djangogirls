from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post Information', {'fields': ['author', 'title', 'text']}),
        ('Date Information', {'fields': ['date_created', 'date_published']}),
    ]
    list_display = ['title', 'author', 'date_created', 'date_published']


admin.site.register(Post, PostAdmin)
