from django.db import models

# Create your models here.
class variant_oge(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to ='oge/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вариант ОГЭ'
        verbose_name_plural = 'Варианты ОГЭ'