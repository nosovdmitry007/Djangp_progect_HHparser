from django.db import models
from usersapp.models import ParserUser
# Create your models here.
class Params(models.Model):
    name_search = models.TextField(blank=True,verbose_name='Name search')
    where_search = models.CharField(max_length=32,verbose_name='Where search')
    user = models.ForeignKey(ParserUser, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name_search}, {self.where_search}'
    class Meta:
        verbose_name='Params'

class Skills_table(models.Model):
    skil = models.CharField(max_length=60,verbose_name='Skil')
    user = models.ForeignKey(ParserUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.skil}'

    class Meta:
        ordering = ('skil',)
        verbose_name = 'Skills table'


class Vacancy(models.Model):
    name = models.TextField(blank=True,verbose_name='name')
    salary = models.CharField(max_length=32,verbose_name='Salary')
    about = models.TextField(blank=True,verbose_name='About')
    link = models.TextField(blank=True,verbose_name='Link')
    comment = models.TextField(blank=True,verbose_name='Commentary')
    user = models.ForeignKey(ParserUser, on_delete=models.CASCADE)
    skils = models.ManyToManyField(Skills_table)

    def __str__(self):
        return f'{self.name}, {self.salary}, {self.about}, {self.link}, {self.skils}'

    class Meta:
        ordering = ('link',)
        verbose_name = 'Vacancys'