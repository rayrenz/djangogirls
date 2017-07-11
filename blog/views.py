from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import Post


class PostListView(generic.ListView):
    context_object_name = 'published_post_list'
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(date_published__lte=timezone.now())
