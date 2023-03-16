from django.db import models

class Articles(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Название', max_length=255)
    anons = models.CharField('Анонс', max_length=500)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикаций')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'


    class Meta():
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
