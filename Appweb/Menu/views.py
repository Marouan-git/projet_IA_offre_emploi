from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from Menu.Fonction import scrap_offre
from .forms import Filtreform
from .models import pole

# Create your views here.

#Dash board
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
    return render (request,'Menu/index.html')

 

#Apps
def calendar(request):
    return render (request,'Menu/calendar.html')

def chat(request):
    return render (request,'Menu/chat.html')  
    



def dashboarddmap(request):

    '''data = scrap_offre.request_offers(id="PAR_offria_53dfa31d974f0c1f80ff7ff26d273e99ae0200e44147654b2f2ecdbfcfa2169c",
                                        secret_key="8d6e4dd17d3ca12937e031235b836057ce7ce9e151bd80396fa9133db9fe823d")'''

    '''for index,row in data.iterrows():

        pole.objects.get_or_create(
            intitule=row["intitule"],
            description=row["description"],
            dateCreation=row["dateCreation"],
            dateActualisation=row["dateActualisation"],
            latitudeLieuTravail= row["latitudeLieuTravail"],
            longitudeLieuTravail=row["longitudeLieuTravail"],
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
           )'''         

    coord = {'bdd' : pole.objects.all(),
        }
    return render(request, 'Menu/mapdash.html',context=coord)


def calendar(request):
    return render (request,'Menu/calendar.html')

def avancer(request):
    if request.method == "POST":
        form = Filtreform(request.POST)
        if form.is_valid():
            intitule = form.cleaned_data['intitule']
            
            coord = {'bdd' : pole.objects.raw(f"""SELECT * FROM  Menu_pole WHERE intitule LIKE  '%{intitule}%' ;"""),
            } 
            
          
            
            return render(request, 'Menu/avancer.html',{"context":coord,'form': form},)    
    

    else:
        form = Filtreform()  
            
    coord = {'bdd' : pole.objects.all(),
        } 
    return render (request,'Menu/avancer.html',{'form': form})


