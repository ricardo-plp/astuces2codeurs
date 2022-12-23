from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published')
    )
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10 , default='draft')
    publish = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posted')



