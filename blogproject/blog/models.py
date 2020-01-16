import markdown
from django.utils.html import strip_tags
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse 

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Tag(models.Model):

    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Post(models.Model):

    # the title of the post
    title = models.CharField(max_length = 100)
    # the body content of the post
    body = models.TextField()
    # the time when a post was created 
    created_time = models.DateTimeField()
    # the time when a post was modified 
    modified_time = models.DateTimeField()
    # the excerpt of a post
    excerpt = models.CharField(max_length = 300, blank = True)
    # the category of a post. One post has only one category, but one category includes one or more posts.
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    # the tag of a post. One post can have multiple tags.
    tags = models.ManyToManyField(Tag, blank = True)
    # author of a post. The "User" here was imported from django.contrib.auth.models 
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        self.excerpt = strip_tags(md.convert(self.body))[:54]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time', 'title']

