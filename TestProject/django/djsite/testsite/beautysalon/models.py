from django.db import models

class HeaderMedia(models.Model):
    name = models.CharField(max_length=255 ,null=True, verbose_name="Название сервиса")
    social_image_header = models.ImageField(null=True, blank=True, upload_to="images/")
    url = models.CharField(max_length=1000 ,null=True, verbose_name="Ссылка на сервис")

    class Meta:
        verbose_name = 'Соц сеть'
        verbose_name_plural = 'Соц сети'

class HomeMedia(models.Model):
    title = models.CharField(max_length=255, null=True)
    home_image = models.ImageField(null=True, blank=True, upload_to="images/")