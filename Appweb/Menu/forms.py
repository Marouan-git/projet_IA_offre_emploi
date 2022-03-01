from .models import *
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class Filtreform(forms.Form):
    Liste_intitule = [("SCIENTIST","Scientist"),("ANALYST",'Analyst'),("manager",'Manager'),("ENGINEER",'Engineer'),("Developpeur",'Developpeur'),("Miner",'Miner')]
    liste_alternance = [("True","True"),("False",'False')]
    liste_langue = [("en","EN"),("fr",'FR')]

    intitule = forms.ChoiceField(choices=Liste_intitule)
    alternance = forms.ChoiceField(choices=liste_alternance)
    langue = forms.ChoiceField(choices=liste_langue)
    date_debut =forms.DateField(widget=DateInput())
    date_fin = forms.DateField(widget=DateInput())
 

class CVForm(forms.Form):
    file = forms.FileField()  # for creating file input


class trad(forms.Form):
      id = forms.IntegerField()
      
      
class bot(forms.Form):
      demande = forms.CharField(max_length=1000)
      
      
      
      

class profile(forms.Form):
    id = forms.IntegerField()
    text = forms.CharField(max_length=300)