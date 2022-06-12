# Generated by Django 4.0.1 on 2022-06-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oge', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blockalgebraoge',
            options={'verbose_name': 'Программа блока Алгебра ОГЭ', 'verbose_name_plural': 'Программы блоков Алгебра ОГЭ'},
        ),
        migrations.AlterModelOptions(
            name='blockgeometriaoge',
            options={'verbose_name': 'Программа блока Геометрия ОГЭ', 'verbose_name_plural': 'Программы блоков Геометрия ОГЭ'},
        ),
        migrations.AlterModelOptions(
            name='variantoge',
            options={'verbose_name': 'Вариант ОГЭ', 'verbose_name_plural': 'Варианты ОГЭ'},
        ),
        migrations.AlterField(
            model_name='blockalgebraoge',
            name='file_algebra_oge',
            field=models.FileField(upload_to='algebra/', verbose_name='Файл блока'),
        ),
        migrations.AlterField(
            model_name='blockalgebraoge',
            name='title_algebra_oge',
            field=models.CharField(max_length=255, verbose_name='Название блока'),
        ),
        migrations.AlterField(
            model_name='blockgeometriaoge',
            name='file_geometria_oge',
            field=models.FileField(upload_to='geometria/', verbose_name='Файл блока'),
        ),
        migrations.AlterField(
            model_name='blockgeometriaoge',
            name='title_geometria_oge',
            field=models.CharField(max_length=255, verbose_name='Название блока'),
        ),
        migrations.AlterField(
            model_name='variantoge',
            name='file_oge',
            field=models.FileField(upload_to='ege/', verbose_name='Файл варианта'),
        ),
        migrations.AlterField(
            model_name='variantoge',
            name='title_oge',
            field=models.CharField(max_length=255, verbose_name='Номер варианта'),
        ),
    ]
