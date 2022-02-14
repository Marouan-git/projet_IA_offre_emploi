from django.shortcuts import render

# Create your views here.
#Vertical
def darksidebar(request):
    greeting={}
    greeting['title']="Dark Sidebar"
    greeting['path']="Vertical"
    return render (request,'Layouts/Vertical/darksidebar.html',greeting)      

def compactsidebar(request):
    greeting={}
    greeting['title']="Compact Sidebar"
    greeting['path']="Vertical"
    return render (request,'Layouts/Vertical/compactsidebar.html',greeting)      
    
def iconsidebar(request):
    greeting={}
    greeting['title']="Icon Sidebar"
    greeting['path']="Vertical"
    return render (request,'Layouts/Vertical/iconsidebar.html',greeting)   

def layoutboxed(request):
    greeting={}
    greeting['title']="Box Width "
    greeting['path']="Vertical"
    return render (request,'Layouts/Vertical/layoutboxed.html',greeting)    

def preloader(request):
    greeting={}
    greeting['title']="Preloader "
    greeting['path']="Vertical"
    return render (request,'Layouts/Vertical/preloader.html',greeting)    

def colorsidebar(request):
    greeting={}
    greeting['title']="Colored Sidebar"
    greeting['path']="Vertical"
    return render (request,'Layouts/Vertical/colorsidebar.html',greeting)     

#Horizontal
def horizontal(request):
    greeting={}
    greeting['title']="Horizontal"
    greeting['path']="Layout"
    return render (request,'Layouts/Horizontal/horizontal.html',greeting)        

def horitopdark(request):
    greeting={}
    greeting['title']="Topbar Dark"
    greeting['path']="Horizontal"
    return render (request,'Layouts/Horizontal/horitopdark.html',greeting)            

def horibox(request):
    greeting={}
    greeting['title']="Box Width"
    greeting['path']="Horizontal"
    return render (request,'Layouts/Horizontal/horibox.html',greeting)   

def horipreloader(request):
    greeting={}
    greeting['title']="Preloader"
    greeting['path']="Horizontal"
    return render (request,'Layouts/Horizontal/horipreloader.html',greeting)   