# Generated by Django 4.0.2 on 2022-06-10 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant_oge',
            name='file',
            field=models.FileField(upload_to='oge/'),
        ),
    ]
