from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class Question(models.Model):
    def __str__(self):
        return self.pregunta

    pregunta = models.CharField(max_length=200)


@python_2_unicode_compatible
class Personaje(models.Model):
    def __str__(self):
        return self.nombre

    nombre = models.CharField(max_length=25)
    votos = models.IntegerField(default=0)


@python_2_unicode_compatible
class Answer(models.Model):
    def __str__(self):
        return self.respuseta

    respuseta = models.CharField(max_length=25)
    usuario = models.ForeignKey(Personaje)
    pregunta = models.ForeignKey(Question)
