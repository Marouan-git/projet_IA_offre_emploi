from django.db import connection
import pandas as pd
from collections import Counter
import re
import nltk

competence_demande = []

def requetage(): 
    '''
    Parametre indiquer une liste de like dans un varaible nommer like_count
    Cela renvoi le result sous forme de dict avec vos mots clés
    Mot cle max 4 a stocker dans la liste
    '''  
    
    
    like_count =["Scientist","Engineer","Analyst","Manager"] 
    nombre_retour_bdd_annonce = {like_count[0]:[], like_count[1]:[], like_count[2]:[], like_count[3]:[]}
    i = 0
    with connection.cursor() as curs:
        for nombre_annonce in like_count:
            curs.execute(f"select count(\"Intitule\") FROM \"Menu_Pole\" WHERE \"Intitule\" LIKE '%{nombre_annonce}%';")
            nombre_retour_bdd_annonce[like_count[i]].append(curs.fetchone()[0])
            i += 1      

    return nombre_retour_bdd_annonce
        


def creation_liste_techno():
    PROG_LANG_KEYWORDS = ['R', 'Python', 'Java', 'C++', 'Ruby', 'Perl', 'Matlab', 'JavaScript', 'Scala']
    ANALYSIS_TOOL_KEYWORDS = ['Excel', 'Tableau', 'D3.js', 'SAS', 'SPSS', 'D3']
    HADOOP_KEYWORDS = ['Hadoop', 'MapReduce', 'Spark', 'Pig', 'Hive', 'Shark', 'Oozie', 'ZooKeeper', 'Flume', 'Mahout']
    DATABASE_KEYWORDS = ['SQL', 'NoSQL', 'HBase', 'Cassandra', 'MongoDB']
    DATA_SCI_KEYWORDS = PROG_LANG_KEYWORDS + ANALYSIS_TOOL_KEYWORDS + HADOOP_KEYWORDS + DATABASE_KEYWORDS
    return DATA_SCI_KEYWORDS



def nbr_techno_trouver_descriptif():
    dico_count = {'R': 0, 'Python': 0, 'Java': 0, 'C++': 0, 'Ruby': 0, 'Perl': 0, 'Matlab': 0, 'JavaScript': 0, 'Scala': 0, 'Excel': 0, 'Tableau': 0, 'D3.js': 0, 'SAS': 0, 'SPSS': 0, 'D3': 0, 'Hadoop': 0, 'MapReduce': 0, 'Spark': 0, 'Pig': 0, 'Hive': 0, 'Shark': 0, 'Oozie': 0, 'ZooKeeper': 0, 'Flume': 0, 'Mahout': 0, 'SQL': 0, 'NoSQL': 0, 'HBase': 0, 'Cassandra': 0, 'MongoDB': 0}
    DATA_SCI_KEYWORDS=creation_liste_techno()
    stop_words = set(nltk.corpus.stopwords.words('french'))
    delete_matching = "[^a-zA-Z.+3]"
    requete = "SELECT description FROM Menu_Pole;"
    df = pd.read_sql(requete,connection)
    description = list(df['description'])
    nombre_annonce = len(description)
    for lin in description:
        lines = lin.strip().splitlines()
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ''.join(f'{chunk} ' for chunk in chunks if chunk).encode('utf-8')
        text = text.decode('unicode_escape')
        text = text.replace('é',"e")
        text = text.replace('è',"e")
        text = text.replace('ê',"e")
        text = text.replace('à',"e")
        text = text.replace("Ã","e")
        text = text.replace('©','e')
        text = text.replace('û','u')
        text = text.replace("»","e")
        text = re.sub(delete_matching, " ", text)
        text = text.lower().split()
        words = []
        keywords_lower = [x.lower() for x in DATA_SCI_KEYWORDS]
        for w in text:    
            if w not in keywords_lower:        
                w = w.replace('.', '')
            if w not in stop_words and len(w) > 0:
                words.append(w)
        all_words = list(set(words))
        freqs = Counter(all_words)
        out_dict = dict([(x, freqs[x.lower()]) for x in DATA_SCI_KEYWORDS])
        df = pd.DataFrame.from_dict(out_dict, orient='index', columns=['Frequency']).reset_index()
        df = df.rename(columns={'index': 'Keyword'}).sort_values(by='Frequency', ascending=False).reset_index(drop=True)
        df.loc[df['Frequency'] > 0]
        for key,value in out_dict.items():
            if value == 1:
                dico_count[key]+=value

    return dico_count,nombre_annonce