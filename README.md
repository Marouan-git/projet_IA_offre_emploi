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
- Une fonction de traduction des offres (toute langue --> français | français --> anglais)
- Un prototype de chatbot qui apporte une assistance à l'utilisateur dans sa candidature
- Une aide à la candidature matérialisée par une redirection vers des liens contenant divers conseils (pour la rédaction du CV, l'entretien d'embauche...)

# Lancement de l'application en local

Cloner le projet :

`git clone url_repo`

Se déplacer dans le dossier Appweb :

`cd Appweb`

Exécuter la commande suivante :

`python manage.py runserver`


# Modèles utilisés

Ci-dessous une brève description des modèles utilisés pour ajouter des fonctionnalités intelligentes à l'application.

## Azure Named Entity Recognition (NER) et modèle naïf correspondant

Fichiers correspondant : ner_skills.py et skills_naif.py

L'API d'Azure Named Entity Recognition et le modèle naïf correspondant nous ont servi à identifier les compétences présentes dans le CV pdf de l'utilisateur pour les faire correspondre à une liste d'offres contenant les compétences extraites du CV.

### Azure NER

1ère étape : extraire les entités (Personnes, organisations, compétences...) du CV pdf fourni par l'utilisateur.
Paramètres à fournir : clé API Azure, endpoint du service d'Azure (cognitive services), nom du fichier pdf correspondant au CV.

```py
from ner_skills import extract_entities, extract_skills_from_entities

entities = extract_entities(API_key, endpoint, CVpdf)
```

2ème étape : extraire les compétences des entités.
Paramètre à fournir : les entités extraites du texte à l'aide de l'API d'Azure. 

```py
skills = extract_skills_from_entities(entities)
print(skills)
```

### Modèle naïf d'extraction des compétences d'un CV pdf

Ce modèle naïf se base sur une liste de compétences liées à la data et l'IA pré-définie (non exhaustive). Il extrait toutes les compétences du CV appartenant à cette liste.
Paramètre à fournir : nom du fichier pdf correspondant au CV.

```py
from skills_naif import extract_skills_resume

skills = extract_skills_resume(CVpdf)
print(skills)
```

## Keywords extraction (KeyBERT)

Fichier correspondant : keywords.py

KeyBERT est un projet Python qui a pour but de simplifier l'extraction de mots-clés d'un texte.
Ce modèle nous a servi à extraire les mots-clés de la description d'une offre pour laquelle l'utilisateur aimerait postuler.
Ces mots-clés sont ensuite utilisés pour adapter la génération de la lettre de motivation à la description de l'offre en question.

Paramètres à fournir : le texte dont on veut extraire les mots-clés, le nombre de mots-clés à extraire.

```py
from keywords import extract_keywords

keywords = extract_keywords(text, nb_keywords)
print(keywords)
```

## Génération d'une lettre de motivation avec le module de complétion de l'API OpenAI

Fichier correspondant : cover_letter.py

L'API d'OpenAI fournit un service de complétion permettant de générer du texte à partir d'un bout de texte écrit par l'utilisateur.
Nous l'avons utilisé pour générer une lettre de motivation adaptée à l'offre sélectionnée par l'utilisateur et à son profile.

Paramètres à fournir : intitulé de l'offre, mots-clés de l'offre, profil de l'utilisateur, clé de l'API

```py
from cover_letter import cover_letter

letter = cover_letter(intitule, keywords, profile, APIkey)
print(letter)
```

## Détection du langage et traduction

Fichier correspondant : traduction.py

Les bibliothèques python utilisées sont langdetect et deeptranslator. La première permet de détecter le langage utilisé dans le texte et la seconde permet de le traduire.

Paramètre à fournir : texte à traduire

```py
from traduction import translate

texte_traduit = translate(text)
print(texte_traduit)
```




