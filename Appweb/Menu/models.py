from typing import OrderedDict
from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey, ManyToManyField




class pole(models.Model):

    intitule = models.TextField()
    description = models.TextField()
    dateCreation = models.DateField()
    dateActualisation =models.DateField()
    latitudeLieuTravail = models.TextField(default='Non renseigné')
    longitudeLieuTravail =models.TextField(default='Non renseigné')
    entreprise = models.TextField()
    typeContrat = models.TextField()
    experienceExigee = models.TextField()
    salaire = models.TextField()
    dureeTravail = models.TextField()
    rythmeTravail = models.TextField()
    alternance = models.TextField()
    nomContact = models.TextField()
    qualification = models.TextField()
    qualitesPro = models.TextField()
    origineOffre = models.TextField()

    def __str__(self):
        return (f'{self.intitule} -- {self.entreprise}')




