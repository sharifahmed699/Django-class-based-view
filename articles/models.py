from django.db import models
from django.utils.text import slugify

# Create your models here.


class Article(models.Model):
    title=models.CharField(max_length=150)
    slug=models.SlugField(null=True,blank=True)
    body=models.TextField()
    create_date=models.DateTimeField(auto_now_add=True)
    is_public=models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug=slugify(self.title)
        super().save(*args, **kwargs)
    

class Comment(models.Model):
    article=models.ForeignKey(Article, on_delete=models.CASCADE)
    comment=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment