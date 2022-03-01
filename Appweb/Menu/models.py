from typing import OrderedDict
from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey, ManyToManyField




class pole(models.Model):

    intitule = models.TextField()
    description = models.TextField()
    dateCreation = models.DateField(null=True)
    latitudeLieuTravail = models.TextField(default='Non renseigné')
    longitudeLieuTravail =models.TextField(default='Non renseigné')
    nomLieuTravail=models.TextField(default='Non renseigné')
    entreprise = models.TextField(default='Non renseigné')
    typeContrat = models.TextField(default='Non renseigné')
    experienceExigee = models.TextField(default='Non renseigné')
    salaire = models.TextField(default='Non renseigné')
    dureeTravail = models.TextField(default='Non renseigné')
    rythmeTravail = models.TextField(default='Non renseigné')
    alternance = models.TextField(default='Non renseigné')
    nomContact = models.TextField(default='Non renseigné')
    qualification = models.TextField(default='Non renseigné')
    qualitesPro = models.TextField(default='Non renseigné')
    origineOffre = models.TextField(default='Non renseigné')
    provenance = models.TextField()
    lang_detect = models.TextField()
    nbSkills = models.IntegerField(default=0)
    matchedSkills = models.TextField(default=" ")



    def __str__(self):
        return (f'{self.intitule} -- {self.provenance}')




