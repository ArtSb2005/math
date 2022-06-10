from django.db import models

# Create your models here.
class variant_ege(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to ='ege/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вариант ЕГЭ'
        verbose_name_plural = 'Варианты ЕГЭ'