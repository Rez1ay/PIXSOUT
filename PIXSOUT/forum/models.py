from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тема форума'
        verbose_name_plural = 'Темы форума'


class Publication(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'{self.author, self.text[:24]}'

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
