from django.db import models
from ckeditor.fields import RichTextField


class UmraDuo(models.Model):
    name = models.CharField(max_length=331)
    audio = models.FileField(upload_to='duos/')
    description = RichTextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Umra Duolari'
        verbose_name_plural = 'Umra Duolari'
