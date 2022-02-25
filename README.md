# Projet 2 - Groupe 2

Membres du groupe 2 : Kamel, Marouan, Aissa

# Présentation de l'application

Application Django qui a pour but d'aider les personnes dans leur recherche d'emploi dans le domaine de la data et de l'IA.  

Cette application contient :

- Un dashboard présentant des statistiques sur les offres disponibles
- Une cartographie des offres dans toute la France
- Un système de recherche avancée qui permet d'afficher les offres d'emploi correspondant à certains critères (métier, date, mots-clés...)
- Un système de recommandation d'offres basé sur les compétences du CV de l'utilisateur
- Un système de génération de lettre de motivation adaptée à l'intitulé et aux mots-clés d'une offre sélectionnée par l'utilisateur ainsi qu'à son profil 
- Une fonction de traduction des offres (anglais --> français | français --> anglais)
- Un chatbot qui apporte une assistance à l'utilisateur dans sa candidature

# Modèles utilisés

Les modèles utilisés pour ajouter des fonctionnalités intelligentes à l'application se trouvent dans la branche model. Ci-dessous une brève description de chacun des modèles utilisés.

## Azure Named Entity Recognition (NER) et modèle naïf correspondant

Fichiers correspondant : ner_skills.py et skills_naif.py

L'API d'Azure Named Entity Recognition et le modèle naïf correspondant nous ont servi à identifier les compétences présentes dans le CV pdf de l'utilisateur pour les faire correspondre à une liste d'offres contenant les compétences extraites du CV.

### Azure NER

1ère étape : extraire les entités (Personnes, organisations, compétences...) du CV pdf fourni par l'utilisateur :

```py
from ner_skills import extract_entities, extract_skills_from_entities

entities = extract_entities(API_key, endpoint, CVpdf)
```

2ème étape : extraire les compétences des entités :

```py
skills = extract_skills_from_entities(entities)
print(skills)
```

### Modèle naïf d'extraction des compétences d'un CV pdf

```py
from skills_naif import extract_skills_resume

skills = extract_skills_resume(CVpdf)
print(skills)
```

## Keywords extraction (KeyBERT)

KeyBERT est un projet Python qui a pour but de simplifier l'extraction de mots-clés d'un texte 



