from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import folium
import geocoder
from django.core.files import File
from .models import States, TemplesData
from folium.plugins import Fullscreen
# Create your views here.

def home(request):
    return render(request,'Temple/home.html')

def direct(request):
    #create map object and popup
    m = folium.Map(location=[22.167057857886153, 82.44140625000001], zoom_start=5)
    borderStyle={
        "color":"green",
        "weight":2,
        "fill":False
    }
    #border for india
    layer1 = folium.GeoJson(data=(open("D:/project1/mini_project/Project/Temple/templates/Temple/states_india.geojson", 'r').read()),name="India",style_function=lambda x:borderStyle).add_to(m)
    #full screen button in map
    Fullscreen(position='topright',title='Expand me',title_cancel='Exit me',force_separate_button=True).add_to(m)
    ob=States.objects.all()
    for i in ob:
        v=i.lat
        l=i.long
        temple = TemplesData.objects.get(id = i.id)
        tooltip=temple.place
        folium.Marker(location=[v,l],popup='<a href="http://127.0.0.1:8000/temple/'+str(i.id)+'" target="blank">'+str(temple.name)+'</a>',icon=folium.Icon(color='red',prefix='fa',icon='bell'),max_bound=True,tooltip=tooltip).add_to(m)

    #get html representation of map object
    m=m._repr_html_()
    context={   
        'm':m,
    }
    return render(request,'Temple/direct.html',context)

def about(request):
    return render(request,'Temple/about.html')

def temple(request,id):
    temple = TemplesData.objects.get(id=id)
    name = temple.name
    place = temple.place
    history = temple.history
    timings = temple.darshtim
    pooja = temple.puja
    food = temple.food
    income = temple.income
    return render(request,'Temple/temple.html',{'id':id,'history':history,'name':name,'place':place,'timings':timings,'pooja':pooja,'food':food,'income':income})
