from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post

# Create your views here.

# 1 version
# def post_list(request):
#     posts = Post.objects.get_queryset().filter(status='published')
#     return render(request, 'blog/post/list.html', {'posts': posts})

# 2 version (Pagination)
# def post_list(request):
#     object_list = Post.objects.get_queryset().filter(status='published')
#     paginator = Paginator(object_list, 3)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)

#     return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})

# 3 version (class-based views)
class PostListView(ListView):
    queryset = Post.objects.get_queryset().filter(status='published')
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    # render  -->  return HttpResponse onject
    return render(request, 'blog/post/detail.html', {'post': post})