from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



# global variables - all/most views use
categories = Category.objects.all()  # Must be visible in sidebar; which all views tend to use
recent_posts = Post.objects.all()[:6]    # Six most recent posts also in sidebar.


# Create your views here.
def index(request):
    posts = Post.objects.all()

    paginator = Paginator(posts, 4)  # 4 posts per page
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # if page is out of range, deliver last page of results
        post_list = paginator.page(paginator.num_pages)


    context = {
        'posts': post_list,
        'page': page,
        'categories': categories,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog/index.html', context)


# we could call this view either with post id or slug
def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)       # Post.objects.get(slug=slug)
    comments = post.comments.filter(active=True)        # All active comments associated with this posts
    new_comment = None

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)    # pass in the data received to the CommentForm
        if comment_form.is_valid():

            # Create a comment but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'categories': categories,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog/detail.html', context)


# could have used the category_id
def category(request, category_tag):
    cat = Category.objects.get(tag=category_tag)
    posts = cat.posts.all()
    context = {
        'cat_name': category_tag,
        'posts': posts,
        'categories': categories,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog/category.html', context)
