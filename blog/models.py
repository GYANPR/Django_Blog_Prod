from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.username}"


class Category(models.Model):
    tag = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.tag}"


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # overview = models.CharField()
    image = models.ImageField(upload_to='post_images', blank=True)
    slug = models.SlugField(max_length=130, unique=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='posts')

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=64)
    email = models.EmailField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment: {self.content[:20]} by {self.name}'