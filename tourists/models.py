from django.db import models

# Create your models here.

class Tourist(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    #documents
    pasport = models.FileField()
    visa = models.FileField()

    hotel = models.ManyToManyField('Hotel', verbose_name='Отель')
    excursion = models.ManyToManyField('Excursion', verbose_name='Экскурсии')
    food = models.ManyToManyField('Food', verbose_name='Питание')

    
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('name',)


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    addres = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    def __str__(self):
        return self.name


class Excursion(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Food(models.Model):
    type = models.CharField(max_length=200)
    time = models.TimeField()
    cost = models.DecimalField(max_digits=7, decimal_places=2)

def __str__(self):
        return self.type