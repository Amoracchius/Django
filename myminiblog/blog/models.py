from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    biography = models.TextField(max_length=2000, help_text='Enter your biography')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    public_date = models.DateField(default=date.today)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['public_date']

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Comments(models.Model):
    public_date = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=1000, help_text="Enter your comment here")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        ordering = ['public_date']

    def __str__(self):
        len_title = 75
        if len(self.content) > len_title:
            title_string = self.content[:len_title] + '. . .'
        else:
            title_string = self.content
        return title_string





