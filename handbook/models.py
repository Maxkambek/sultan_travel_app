from django.db import models
from ckeditor.fields import RichTextField


class Handbook(models.Model):
    name = models.CharField(max_length=221)
    description = RichTextField()
    some_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Umra Qo'llanmasi"
        verbose_name_plural = "Umra Qo'llanmasi"
