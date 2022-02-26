from this import d
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from Menu.Fonction import scrap_offre,traduction,botchat,graphique
from .Fonction.skills_naif import extract_skills_resume
from .Fonction.keywords import extract_keywords
from .Fonction.cover_letter import cover_letter
from .forms import Filtreform,CVForm,trad,profile,bot
from .models import pole
from django.db.models import F
from django.db import connection





def login(request):
    if 'username'  in request.session:
        return redirect('index')
    else:    
        if request.method == 'POST':
            username = request.POST.get("username", "default value")
            userpassword = request.POST.get("userpassword", "default value")
            user = auth.authenticate(username=username, password=userpassword)

            if user is not None:
                request.session['username'] = username
                auth.login(request, user)                
                return redirect("/")
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('login')
        else:
            return render(request, 'Authentication/login.html')
            
def index(request):
    occurence = graphique.requetage()
    n,d = graphique.nbr_techno_trouver_descriptif()
    dic_occ = dict(sorted(n.items(),reverse=True, key=lambda item: item[1]))
    coord = {'bdd':occurence ,
             'occ' : dic_occ}
    
    return render (request,'Menu/index.html',context = coord)

def calendar(request):
    return render (request,'Menu/calendar.html')

    
def dashboarddmap(request):
    
    if request.method == "POST":
        form = Filtreform(request.POST)
        if form.is_valid():
            intitule = form.cleaned_data['intitule']
            alternance = form.cleaned_data['alternance']
            date_debut = form.cleaned_data['date_debut']
            date_fin = form.cleaned_data['date_fin']   
     
            
            coord = {'bdd' : pole.objects.raw(f"""SELECT * FROM  Menu_pole WHERE intitule LIKE  '%{intitule}%'  and alternance LIKE '%{alternance}%' AND dateCreation BETWEEN '{date_debut}' AND '{date_fin}';"""),
            } 

            return render(request, 'Menu/mapdash.html',{"context":coord,'form': form},)    
    
    else:
        form = Filtreform()  
            
    coord = {'bdd' : pole.objects.all(),
        }       

    return render(request, 'Menu/mapdash.html',{"context":coord,'form': form})

def avancer(request):
    if request.method == "POST":
        form = Filtreform(request.POST)
        if form.is_valid():
            intitule = form.cleaned_data['intitule']
            alternance = form.cleaned_data['alternance']
            langue = form.cleaned_data['langue'] 
            date_debut = form.cleaned_data['date_debut']
            date_fin = form.cleaned_data['date_fin']         

     
            
            coord = {'bdd' : pole.objects.raw(f"""SELECT * FROM  Menu_pole WHERE intitule LIKE  '%{intitule}%'  and alternance LIKE '%{alternance}%' AND dateCreation BETWEEN '{date_debut}' AND '{date_fin}' and lang_detect LIKE '%{langue}%' ;"""),
            } 

            return render(request, 'Menu/avancer.html',{"context":coord,'form': form},)    
    
    else:
        form = Filtreform()  
            
    coord = {'bdd' : pole.objects.all(),
        } 
    return render (request,'Menu/avancer.html',{"context":coord,'form': form})

def maj_offre(request):    
    """data_pole= scrap_offre.request_offers(id="PAR_offria_53dfa31d974f0c1f80ff7ff26d273e99ae0200e44147654b2f2ecdbfcfa2169c",
                                        secret_key="8d6e4dd17d3ca12937e031235b836057ce7ce9e151bd80396fa9133db9fe823d")
        
    data_pole['lang_detect'] = data_pole['description'].apply(scrap_offre.language_detect)
    
    for index,row in data_pole.iterrows():

        pole.objects.get_or_create(
            intitule=row["intitule"],
            description=row["description"],
            dateCreation=row["dateCreation"],
            latitudeLieuTravail= row["latitudeLieuTravail"],
            longitudeLieuTravail=row["longitudeLieuTravail"],
            nomLieuTravail=row["nomLieuTravail"],
            entreprise = row["entreprise"],
            typeContrat = row["typeContrat"],
            experienceExigee=row["experienceExigee"],
            salaire= row["salaire"],
            dureeTravail=row["dureeTravail"],
            rythmeTravail = row["rythmeTravail"],
            alternance = row["alternance"],
            nomContact = row["nomContact"],
            qualification = row["qualification"],
            qualitesPro = row["qualitesPro"],
            origineOffre = row["origineOffre"],
            provenance = row['provenance'],
            lang_detect = row['lang_detect'],

           )
           
    data_indeed = scrap_offre.offre_indeed()
    data_indeed['lang_detect'] = data_indeed['description'].apply(scrap_offre.language_detect)

          
    for index,row in data_indeed.iterrows():
        
        pole.objects.get_or_create(
            intitule=row["intitule"],
            entreprise=row["entreprise"],
            nomLieuTravail=row["nomLieuTravail"],
            dateCreation=row["dateCreation"],
            latitudeLieuTravail=row["latitudeLieuTravail"],
            longitudeLieuTravail = row["longitudeLieuTravail"],
            description = row["description"],
            provenance = row['provenance'],
            lang_detect = row['lang_detect'],

                )"""
    
    return render(request,'Menu/maj.html')

def cv(request):
    if request.method == 'POST':
        cv = CVForm(request.POST, request.FILES)
        if cv.is_valid():
            pdf = request.FILES['file']
            skills = extract_skills_resume(pdf)
            
            pole.objects.update(matchedSkills=" ")
            pole.objects.update(nbSkills=0)

            for skill in skills:
                
                pole.objects.filter(description__icontains=skill).update(
                    nbSkills=F("nbSkills") + 1)
                
                with connection.cursor() as cursor:
                    cursor.execute(f"UPDATE Menu_pole SET matchedSkills = matchedSkills || ' ' || '{skill.upper()}' WHERE description LIKE '%{skill}%';")

            req = "SELECT * FROM Menu_pole ORDER BY nbSkills DESC"

            coord = {'bdd': pole.objects.raw(req)}
           
            # HttpResponse(skills)
            return render(request, 'Menu/cv.html', {"context": coord, 'form': cv})
    else:
        cv = CVForm()
        return render(request, "Menu/cv.html", {'form': cv})

def tradu(request):

    if request.method == "POST":
        form = trad(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            requete = pole.objects.raw(f"SELECT id,description FROM Menu_pole WHERE id = {id}")
            
            description = [p.description for p in requete]
            tradu = traduction.translate(description[0])

            coord = {'bdd': tradu } 
    
        return render (request,'Menu/traduction.html',{"context":coord,'form': form})
    else:
        form = trad()
        return render(request, "Menu/traduction.html", {'form': form})

def chatbot(request):
       
    if request.method == "POST":
        form = bot(request.POST)
        if form.is_valid():
            demande = form.cleaned_data['demande']                                               

            bot_call = botchat.get_response(demande)
            print(type(bot_call))
            list_bot_call=  bot_call

            if type(list_bot_call) == list : 
               
               coordo = {'list_call': list_bot_call }

               return render (request,'Menu/chatbot.html',{"context":coordo,'form': form}) 
            else:
                coord = {'bdd': bot_call }  
                return render (request,'Menu/chatbot.html',{"context":coord,'form': form})
    else:
        form = bot()
        return render(request, 'Menu/chatbot.html', {'form': form})

def coverletter(request):
    if request.method == "POST":
        form = profile(request.POST)

        if form.is_valid():
            id = form.cleaned_data['id']
            text = form.cleaned_data['text']
            requete = pole.objects.raw(
                f"SELECT id,description,intitule FROM Menu_pole WHERE id = {id}")
            description = [p.description for p in requete][0]
            intitule = [p.intitule for p in requete][0]
            keywords = extract_keywords(description, 7)
            letter = cover_letter(intitule, keywords, text)

            coord = {'bdd': letter}
        return render(request, 'Menu/coverletter.html', {"context": coord, 'form': form})
    else:
        form = profile()
        return render(request, "Menu/coverletter.html", {'form': form})