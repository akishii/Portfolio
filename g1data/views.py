from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .forms import G1racesForm
from .models import Racedata


# Create your views here.
def index(request):

    params = {
        'form': G1racesForm(),
        'data': [],
    }  
    
    #POST送信時DBからデータを取得
    if (request.method == 'POST'):
        num1 = request.POST['year']
        num2 = request.POST['race_name']
        form = G1racesForm(request.POST)
        data = Racedata.objects.filter(Q(year_id=num1), Q(race_id=num2))  

        params = {
        'form': G1racesForm(),
        'data': data,
    }      

    return render(request, "g1data/index.html", params)
