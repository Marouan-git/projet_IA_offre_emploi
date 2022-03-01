import re
from threading import activeCount
import os
import requests
import unicodedata
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from django.db import connection






def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    messagecertainty = 0, 
    has_required_words = True   

    for word in user_message:
        message_certainty = 0
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))


    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

    
def check_all_messages(message):
    highest_prob_list = {}



    def response(bot_response, list_of_words, single_response=False, required_words = None):
        
        list_of_words = [each_string.lower() for each_string in list_of_words]
                       
        if required_words is None:
            required_words = []
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Salut (:', ['hello', 'hi', 'sup', 'hey', 'salam','heyo', 'salut', 'bonjour', 'ciao', 'bonsoir', 'bye bye', 'alaikum'], single_response=True)  
    response("Ok!, t'as besoin d'aide dans quoi? ", ['help', 'me', 'aide', 'moi'], required_words=['aide']) 
    response("de rien :)", ['merci', 'thank', 'you'], required_words=['merci']) 
    response('Bien et toi?', ["ça", "ca", "vas", 'how', 'are', 'you','doing', 'salut'], required_words=[])
    response('ok, comment puis je t\'aider?', ["bien", "oklm", 'hamdulillah', "au", "calme"], required_words=[])
    response('Thank you!', ['you', 'are', 'really','pretty'], required_words=['pretty', 'you'])
    response("Je m'appelle Jobless et toi?", ['comment', "tu", "t", "'", "appelle", "qui", "est", "tu"], required_words=['appelle'])  
    response("4 ans", ["t", "as", "quel", "age"], required_words=['age'])
    response("Pour des conseilles sur le cv vas sur: https://www.regionsjob.com/conseils/cv", ["cv"], required_words=['cv'])
    response("T'aimerais inclure quoi dans la lettre de motivation?", ["l", "lettre", "de", "motivation"], required_words=['lettre'])
    response("D'accord, envoie moi des keywords pour trouver l'offre plus adequate à toi", ["offres", "rechercher", "data", "emploi", "recherche", "offre"], required_words=[])
  
 

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return best_match

    
"""    response("Pour des conseilles sur le cv vas sur: https://www.regionsjob.com/conseils/cv", ["aide", "moi", "avec", "le", "cv"], required_words=['cv'])
    response("Ok je vais essayer de te la rediger, si tu veut voir comment la faire par soi meme regarde: https://www.regionsjob.com/conseils/lettre-motivation", ["aide", "moi", "avec", "ma", "lettre", "de", "motivation"], required_words=['lettre'])  
    response("Je m'appelle Jobless et toi?", ['comment', "tu", "t", "'", "appelle", "qui", "est", "tu"], required_words=['appelle'])  
    response("Ok, tu recherche quoi?", ['aide', 'moi', 'avec', 'ma', 'recherche', 'd', 'emploi', 'alternance'], required_words=['recherche'])  """
    
        
   
activator = 0

###############
def extract_entities(cog_key, cog_endpoint, text):
    
    def authenticate_client():
        ta_credential = AzureKeyCredential(cog_key)
        text_analytics_client = TextAnalyticsClient(
            endpoint=cog_endpoint,
            credential=ta_credential)
        return text_analytics_client

    client = authenticate_client()

    def entity_recognition(client):

        try:
            documents = [
                {
                    "id": "1",
                    "language": "fr",
                    "text": text,
                }
            ]

            result = client.recognize_entities(documents=documents)[0]

            #print("Named Entities:\n")

            result_dict = {"resultats": []}

            for entity in result.entities:
                # print("\tText: \t", entity.text, "\tCategory: \t", entity.category, "\tSubCategory: \t", entity.subcategory,
                # "\n\tConfidence Score: \t", round(entity.confidence_score, 2), "\tLength: \t", entity.length, "\tOffset: \t", entity.offset, "\n") # Convertir en dico

                res = {
                    'text': entity.text,
                    'category': entity.category,
                    'subcategory': entity.subcategory,
                    'confidence_score': entity.confidence_score,
                    'length': entity.length,
                    'offset': entity.offset,
                }

                result_dict["resultats"].append(res)

        except Exception as err:
            print("Encountered exception. {}".format(err))

        return result_dict
    
    return entity_recognition(client)


def extract_skills_from_entities(entities):
    """ Extrait les skills des entités résultats de l'appel d'API 

        Parameters
        ----------
        entities : dict
            Dictionnaire contenant une liste des dictionnaires correspondant aux différentes entités

        Return
        ------
        skills : list
            Liste des compétences extraites des entités

    """

    skills = []

    for entity in entities['resultats']:
        if entity['category'] == 'Skill' and entity['confidence_score'] > 0.9:
            skills.append(entity['text'])

    return skills

#####

# lettre motivation auto generè

def cover_letter(text):
    
    headers = {'Content-Type': 'application/json',
                'Authorization': f'Bearer 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'}

    url = 'https://api.openai.com/v1/engines/text-davinci-001/completions'

    body = {
        'prompt': f'ecris moi une lettre de motivation qui contient ces carachteristiques: {text}',
        'max_tokens': 1600
    }

    response = requests.post(url, json=body, headers=headers)


    letter = response.json()['choices'][0]['text']

    return letter

import unicodedata

off_activator = 0

def get_response(user_input):
    
    global activator, off_activator
    
    user_input = str(user_input)
    
    user_input = unicodedata.normalize('NFD', user_input).encode('ascii', 'ignore').decode("utf-8")
    user_input = re.sub(r'[^\w\s]',' ',user_input)
    
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
        
    
    response = check_all_messages(split_message)
    if activator == 1:
        activator = 0 
        return cover_letter(user_input)

    if response == "T'aimerais inclure quoi dans la lettre de motivation?":
        activator += 1
        
    if off_activator == 1:
        off_activator = 0 
        
        liste = (user_input.split())
        reponse_requete = []
        for ele in liste:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM  Menu_pole WHERE intitule LIKE '%{ele}%' limit 20")
                records = cursor.fetchall()
                
                for row in records:                    
                    if  row[17] != 'Non renseigné':                  
                        reponse_requete.append({"Intitule" : row[1] ,"Lien" : row[17] })
                   

                    
                    

                     
        return reponse_requete
    if response == "D'accord, envoie moi des keywords pour trouver l'offre plus adequate à toi":
        off_activator += 1
        
    return response


n_times = 0
