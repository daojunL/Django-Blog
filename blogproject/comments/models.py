from django.db import models
from django.utils import timezone

# Create your models here.

class Comment(models.Model):
    name = models.CharField('Name', max_length=50)
    email = models.EmailField('Email')
    text = models.TextField('Comments')
    created_time = models.DateTimeField('Posted on', default = timezone.now)
    post = models.ForeignKey('blog.Post', on_delete = models.CASCADE)

    def __str__(self):
        return '{}:{}'.format(self.name, self.text[:20])
