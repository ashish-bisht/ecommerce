from django.http import HttpResponse
from django .shortcuts import render
from .forms import ContactForm
def home_page(request):
    context = {
        'title': 'Home Page',
        'content':'We gonna make it soon'

    }

    return render(request, 'home.html', context)

def about_page(request):
    return render(request, 'about.html', context={})

def contact_page(request):
    contact_form = ContactForm()
    context = {
        'title':'Contact Page',
        'form':contact_form
    }

    return render(request, 'contact.html', context)
