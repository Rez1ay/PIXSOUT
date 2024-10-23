from django.db import models


class Screenshot(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='screenshots/')

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Скриншот'
        verbose_name_plural = 'Скриншоты'
