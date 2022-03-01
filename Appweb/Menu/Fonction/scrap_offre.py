import requests
from offres_emploi import Api
import pandas as pd
from datetime import datetime
from geopy.geocoders import Nominatim
from functools import partial
import re
import feedparser as fp
import pandas as pd
from geopy.geocoders import Nominatim
from functools import partial
from bs4 import BeautifulSoup
from langdetect import  detect




def request_offers(id="PAR_offria_53dfa31d974f0c1f80ff7ff26d273e99ae0200e44147654b2f2ecdbfcfa2169c", 
                   secret_key="8d6e4dd17d3ca12937e031235b836057ce7ce9e151bd80396fa9133db9fe823d"):
    client = Api(

        client_id=id,
        client_secret=secret_key

    )
    geolocator = Nominatim(user_agent="apps")

    keys = ['intitule', 'description', 'dateCreation', 'dateActualisation', 'nomLieuTravail', 'latitudeLieuTravail', 'longitudeLieuTravail', 'entreprise', 'typeContrat',
            'experienceExigee', 'competences', 'salaire', 'dureeTravail', 'rythmeTravail', 'alternance', 'nomContact', 'qualification', 'secteurActivite', 'qualitesPro', 'origineOffre']

    results = dict(zip(keys, ([] for _ in keys)))

    for i in range(0, 1049, 150):
        param = {
            'range': f"{i}-{i + 149}",
            'motsCles': ['data', 'IA', 'machine learning'],
        }
        response = client.search(param)
        for elem in response['resultats']:

            if 'intitule' in elem.keys():
                results['intitule'].append(elem['intitule'])
            else:
                results['intitule'].append('Non renseigné')

            if 'description' in elem.keys():
                results['description'].append(elem['description'])
            else:
                results['description'].append('Non renseigné')

            if 'dateCreation' in elem.keys():
                dateCreation = datetime.strptime(
                    elem['dateCreation'], '%Y-%m-%dT%H:%M:%S.%fZ')
                results['dateCreation'].append(
                    dateCreation)
            else:
                results['dateCreation'].append('Non renseigné')

            if 'dateActualisation' in elem.keys():
                dateActualisation = datetime.strptime(
                    elem['dateActualisation'], '%Y-%m-%dT%H:%M:%S.%fZ')
                results['dateActualisation'].append(
                    dateActualisation)
            else:
                results['dateActualisation'].append('Non renseigné')

            if 'lieuTravail' in elem.keys():
                results['nomLieuTravail'].append(elem['lieuTravail']['libelle'])
                
                try:
                    ville = elem['lieuTravail']['libelle']

                    if ville.split("-")[1] != "":
                        geocode = partial(geolocator.geocode, addressdetails= True, language="fr")
                        extraction = geocode(ville.split("-")[1])
                        loc = Nominatim(user_agent="GetLoc") 
                        getLoc = loc.geocode(extraction)
                        print(ville.split("-")[1])
                        
                        
                        results['latitudeLieuTravail'].append(getLoc.latitude)
                        results['longitudeLieuTravail'].append(getLoc.longitude)
                        print(getLoc.longitude)
                except:
                    results['latitudeLieuTravail'].append('Non renseigné')
                    results['longitudeLieuTravail'].append('Non renseigné')
            else:
                results['nomLieuTravail'].append('Non renseigné')
                results['latitudeLieuTravail'].append('Non renseigné')
                results['longitudeLieuTravail'].append('Non renseigné')
        
           
            if 'nom' in elem['entreprise'].keys():
                results['entreprise'].append(
                    elem['entreprise']['nom'])
            else:
                results['entreprise'].append('Non renseigné')

            if 'typeContrat' in elem.keys():
                results['typeContrat'].append(
                    elem['typeContrat'])
            else:
                results['typeContrat'].append('Non renseigné')

            if 'experienceLibelle' in elem.keys():
                results['experienceExigee'].append(
                    elem['experienceLibelle'])
            else:
                results['experienceExigee'].append('Non renseigné')

            if 'competences' in elem.keys():
                l = []  # liste des compétences pour une offre donnée
                for dico in elem['competences']:
                    l.append(dico['libelle'])
                results['competences'].append(l)
            else:
                results['competences'].append('Non renseigné')

            if 'libelle' in elem['salaire'].keys():
                results['salaire'].append(
                    elem['salaire']['libelle'])
            else:
                results['salaire'].append('Non renseigné')

            if 'dureeTravailLibelle' in elem.keys():
                results['dureeTravail'].append(
                    elem['dureeTravailLibelle'])
            else:
                results['dureeTravail'].append('Non renseigné')

            if 'dureeTravailLibelleConverti' in elem.keys():
                results['rythmeTravail'].append(
                    elem['dureeTravailLibelleConverti'])
            else:
                results['rythmeTravail'].append('Non renseigné')

            if 'alternance' in elem.keys():
                results['alternance'].append(
                    elem['alternance'])
            else:
                results['alternance'].append('Non renseigné')

            if 'contact' in elem.keys():
                if 'nom' in elem['contact'].keys():
                    results['nomContact'].append(
                        elem['contact']['nom'])
                else:
                    results['nomContact'].append('Non renseigné')
            else:
                results['nomContact'].append('Non renseigné')

            if 'qualificationLibelle' in elem.keys():
                results['qualification'].append(
                    elem['qualificationLibelle'])
            else:
                results['qualification'].append('Non renseigné')

            if 'secteurActiviteLibelle' in elem.keys():
                results['secteurActivite'].append(
                    elem['secteurActiviteLibelle'])
            else:
                results['secteurActivite'].append('Non renseigné')

            if 'qualitesProfessionnelles' in elem.keys():
                l2 = []
                for dico in elem['qualitesProfessionnelles']:
                    l2.append(dico['libelle'])
                results['qualitesPro'].append(l2)
            else:
                results['qualitesPro'].append('Non renseigné')

            if 'origineOffre' in elem.keys():
                if 'urlOrigine' in elem['origineOffre'].keys():
                    results['origineOffre'].append(
                        elem['origineOffre']['urlOrigine'])
                else:
                    results['origineOffre'].append('Non renseigné')
            else:
                results['origineOffre'].append('Non renseigné')

    df = pd.DataFrame.from_dict(results)
    df['provenance'] = "Pole-Emploi"
    return df



def language_detect(x):
        return detect(x)
    
    

def offre_indeed():
    data = {
        "intitule":[],
        "entreprise":[],
        "nomLieuTravail":[],
        "dateCreation":[],
        "lien":[],
        "latitudeLieuTravail":[],
        "longitudeLieuTravail":[], 
        "description":[],  
        
    }

    geolocator = Nominatim(user_agent="apps")
    
    DEPARTMENTS = ["Lyon","Grenoble","Paris","Dijon","Annecy"]

    for ele in DEPARTMENTS:
        
        rss_indeed = f"https://fr.indeed.com/rss?q=data&l={ele}&fromage=last&sort=date"
        d = fp.parse(rss_indeed)
       
        for rows in range(len(d.entries)):

            data["intitule"].append(d.entries[rows].title)
            data["lien"].append(d.entries[rows].links[0].href)

            dateCreation = d.entries[rows].published
            dateCreation = datetime.strptime(dateCreation, '%a, %d %b %Y %H:%M:%S %Z')
            data["dateCreation"].append(dateCreation.date())
            data["entreprise"].append(d.entries[rows].source.title.capitalize())

            lieu = d.entries[rows].title
            m = re.search(r'-(?P<nom_entreprise>.+) - (?P<Lieu>[^()]*)', lieu)
            lieu = m.group(2)

            data["nomLieuTravail"].append(lieu.capitalize())
            
        
            geocode = partial(geolocator.geocode, addressdetails= True, language="fr")
            extraction = geocode(lieu)

            loc = Nominatim(user_agent="GetLoc") 

            getLoc = loc.geocode(extraction) 

            data["latitudeLieuTravail"].append(getLoc.latitude)
            data["longitudeLieuTravail"].append(getLoc.longitude)
            r = requests.get(d.entries[rows].links[0].href)
            soup = BeautifulSoup(r.text, 'html.parser')
            des = soup.find(id="jobDescriptionText").text
            data["description"].append(des)

    df = pd.DataFrame(data)
    df['provenance'] = "Indeed"
    return df
