from django.db import models

# Create your models here.


class Post(models.Model):
    novost = models.CharField('Новость',max_length=300,null=True)
    date = models.DateField('Дата',null=True)
    descp = models.TextField('Описание новости',null=True)
    img = models.ImageField(upload_to='%Y/%m/%d',null=True)
    author = models.CharField('Автор',max_length=100)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return f'{self.novost} {self.date}'

    class Meta():
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'