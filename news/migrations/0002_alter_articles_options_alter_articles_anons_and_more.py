# Generated by Django 4.1.7 on 2023-03-13 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='anons',
            field=models.CharField(max_length=500, verbose_name='Анонс'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
