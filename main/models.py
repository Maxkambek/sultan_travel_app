from django.db import models
from ckeditor.fields import RichTextField


class News(models.Model):
    title = models.CharField(max_length=333)
    content = RichTextField()
    image = models.ImageField(upload_to='news/')
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Yangiliklar'
        verbose_name_plural = 'Yangiliklar'


class Tour(models.Model):
    name = models.CharField(max_length=123)
    price = models.CharField(max_length=50)
    date = models.CharField(max_length=123)
    description = RichTextField()
    image = models.ImageField(upload_to='tour/')

    class Meta:
        verbose_name = 'Tur'
        verbose_name_plural = "Turlar"
