from django.http import HttpResponse
from django.shortcuts import render
from . models import Shoe, About, Service, Contact


def index(request):
    shoes = Shoe.objects.all()
    return render(request, 'index.html', {'shoes': shoes})


def about(request):
    about_us = About.objects.all()
    return render(request, 'about.html', {'about': about_us})


def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})


def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts.html', {'contacts': contacts})