from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.cache import cache
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from blog.models import Post


class HomeView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = cache.get('posts')
        print(posts)
        if posts is None:
            posts = Post.objects.all()
            cache.set('posts', posts, timeout=60*5)
        context['posts'] = Post.objects.all()
        return context


class AllPostsView(ListView):
    model = Post
    template_name = 'blog/all_posts.html'


class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        cache.delete("posts")
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.object.tags.all()
        return context


class ReadLaterView(View):

    def get(self, request):
        context = {}
        posts_id = request.session.get('stored_posts')
        posts = Post.objects.filter(id__in=posts_id)
        if not posts:
            context['posts'] = []
            context['has_posts'] = False
        else:
            context['posts'] = posts
            context['has_posts'] = True

        return render(request, 'blog/stored_posts.html', context)

    def post(self, request):
        post_id = int(request.POST['post_id'])
        stored_posts = request.session.get('stored_posts')
        if not stored_posts:
            stored_posts = []

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session['stored_posts'] = stored_posts

        return HttpResponseRedirect('/')
