from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    code = models.CharField(max_length=200,blank=True,null=True)
    total_posts = models.IntegerField(default=0,blank=True,null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return unicode(self.title)
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    time_published = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=1500,blank=True,null=True) 
    author = models.ForeignKey(User,related_name='author',blank=True,null=True)  
    category = models.ForeignKey(Category,related_name='author',blank=True,null=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return unicode(self.title)


class Comment(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    time_published = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=1500,blank=True,null=True)
    author = models.ForeignKey(User,related_name='comment_author',blank=True,null=True)
    post = models.ForeignKey(Post,related_name='post',blank=True,null=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return unicode(self.title)


# Create your models here.