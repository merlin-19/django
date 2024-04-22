from django.shortcuts import render
from django.http import HttpResponse
from .models import datachange
# Create your views here.
def index(request):
    dest = datachange()
    dest.name = "Goa"
    dest.price = 20000
    dest.desc = "India"
    dest.images = "goa.jpg"
    dest.offer=True

    dest2 = datachange()
    dest2.name = "Red Fort"
    dest2.price = 30000
    dest2.desc = "India"
    dest2.images = "redfort.jpg"
    dest2.offer=True


    dest3 = datachange()
    dest3.name = "Munnar"
    dest3.price = 10000
    dest3.desc = "India"
    dest3.images = "munnar.jpg"
    dest3.offer=True

    dest4 = datachange()
    dest4.name = "Kanyakumari"
    dest4.price = 15000
    dest4.desc = "India"
    dest4.images = "kanyakumari.jpg"
    dest4.offer=True

    dest5 = datachange()
    dest5.name = "Ooty"
    dest5.price = 20000
    dest5.desc = "India"
    dest5.images = "ooty.jpg"
    dest5.offer=True


    dest6 = datachange()
    dest6.name = "Taj Mahal"
    dest6.price = 30000
    dest6.desc = "India"
    dest6.images = "taj.jpg"
    dest6.offer=False



    dests = [dest,dest2,dest3,dest4,dest5,dest6]

    return render(request, 'index.html', {'est':dests})   
