from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

#分类
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

 #标签
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

 #文章
class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateField()
    modified_time = models.DateField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})