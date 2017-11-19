from django.http import HttpResponse
from django .shortcuts import render

def home_page(request):
    return render(request, 'home.html', context={})

def about_page(request):
    return render(request, 'about.html', context={})

def contact_page(request):
    return render(request, 'contact.html', context={})
