from django.db import models
from ckeditor.fields import RichTextField


class Place(models.Model):
    name = models.CharField(max_length=331)
    image = models.ImageField(upload_to='places/')
    description = RichTextField()
    latitude = models.DecimalField(
        max_digits=30, decimal_places=15, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=30, decimal_places=15, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Islom tarixiga oid joylar'
        verbose_name_plural = 'Islom tarixiga oid joylar'
