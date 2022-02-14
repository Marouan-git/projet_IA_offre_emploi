from .models import *
from django import forms


class Filtreform(forms.Form):
	Liste_intitule = [("SCIENTIST","SCIENTIST"),("ANALYST",'ANALYST'),("manager",'manager'),("ENGINEER",'ENGINEER'),
                   ("manager",'manager')]

	intitule = forms.ChoiceField(choices=Liste_intitule)
