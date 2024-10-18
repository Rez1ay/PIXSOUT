from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    objects = models.Manager()


class Publication(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    objects = models.Manager()
