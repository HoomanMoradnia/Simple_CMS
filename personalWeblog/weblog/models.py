from django.db import models
from django.utils.text import slugify
from datetime import datetime
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Article(models.Model):
    POST_STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=POST_STATUS, default='draft')
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            now = datetime.now()
            self.slug = slugify(self.title)+"-"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)
            self.save()

    class Meta:
        ordering = ['-created_at']
        

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('weblog:article_detail', kwargs={'slug': self.slug})

    objects = models.Manager()
    published = PublishedManager()