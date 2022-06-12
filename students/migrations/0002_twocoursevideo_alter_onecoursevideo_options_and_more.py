# Generated by Django 4.0.1 on 2022-06-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwoCourseVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Тема')),
                ('body', models.TextField(verbose_name='Краткая информация')),
                ('video', models.FileField(upload_to='otv/', verbose_name='Видеофайл')),
            ],
            options={
                'verbose_name': 'Видеоуроки 2 курс',
                'verbose_name_plural': 'Видеоуроки 2 курс',
            },
        ),
        migrations.AlterModelOptions(
            name='onecoursevideo',
            options={'verbose_name': 'Видеоуроки 1 курс', 'verbose_name_plural': 'Видеоуроки 1 курс'},
        ),
        migrations.AlterField(
            model_name='onecoursevideo',
            name='body',
            field=models.TextField(verbose_name='Краткая информация'),
        ),
        migrations.AlterField(
            model_name='onecoursevideo',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='onecoursevideo',
            name='video',
            field=models.FileField(upload_to='ocv/', verbose_name='Видеофайл'),
        ),
    ]