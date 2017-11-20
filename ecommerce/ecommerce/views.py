from django.http import HttpResponse
from django .shortcuts import render
from .forms import ContactForm,LoginForm
def home_page(request):
    context = {
        'title': 'Home Page',
        'content':'We gonna make it soon'

    }

    return render(request, 'home.html', context)

def about_page(request):
    return render(request, 'about.html', context={})

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title':'Contact Page',
        'form':contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)




    # if request.method =='POST':
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))

    return render(request, 'contact.html', context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form':form
    }
    print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
    
    return render(request,'auth/login.html',context)

def register_page(request):
    return render(request,'auth/register.html',{})