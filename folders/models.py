from django.db import models
from django.forms import CharField, DateField, FileField
from django.http import FileResponse


class Folders(models.Model):
    title = models.CharField('Штамп Папки', max_length=5)
    descrip = models.CharField('Краткое Описание', max_length=200)
    datecomplited = models.DateField('Дата Добавления Файла', null=True, blank = True)
    file = models.FileField('Выберите Файл', upload_to= 'uploads/%Y/%m/%d/' )

    def __str__(self):
        return self.title
