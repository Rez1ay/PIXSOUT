from django.db import models


class Screenshot(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='screenshots/')

    objects = models.Manager()
