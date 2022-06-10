from django.db import models

# Create your models here.
class cert_main(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to ='cert/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'