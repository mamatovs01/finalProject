from django.db import models

class Photo(models.Model):
    title = models.CharField(default="Noname",max_length=255,verbose_name="Название")
    img = models.ImageField(verbose_name="Фото")
    views = models.PositiveIntegerField(default=0,verbose_name="Просмотры")
    like = models.PositiveIntegerField(default=0,verbose_name="Лайки")
    what = models.CharField(default="Noname",max_length=255,verbose_name="вещи")


