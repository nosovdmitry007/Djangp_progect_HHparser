from django.db import models

# Create your models here.
class Params(models.Model):
    name_search = models.TextField(blank=True)
    where_search = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name_search}, {self.where_search}'

class Skills_table(models.Model):
    skil = models.CharField(max_length=60,unique=True)
    # how_many_skil = models.IntegerField()

    def __str__(self):
        return f'{self.skil}'

    class Meta:
        ordering = ('skil',)

class Vacancy(models.Model):
    name = models.TextField(blank=True)
    salary = models.CharField(max_length=32)
    about = models.TextField(blank=True)
    link = models.TextField(unique=True)
    skils = models.ManyToManyField(Skills_table)

    def __str__(self):
        return f'{self.name}, {self.salary}, {self.about}, {self.link}, {self.skils}'

    class Meta:
        ordering = ('link',)