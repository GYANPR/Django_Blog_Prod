from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import CommentForm


# Create your views here.
def index(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/index.html', context)


# we could call this view either with post id or slug
def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)       # Post.objects.get(slug=slug)
    comments = post.comments.filter(active=True)        # All comments associated with this posts
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
    }
    return render(request, 'blog/detail.html', context)
