from django.db import models


class Preparation(models.Model):
    name = models.CharField(max_length=221)
    text = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Safarga tayyorgarlik'
        verbose_name_plural = 'Safarga tayyorgarlik'
