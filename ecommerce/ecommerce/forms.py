from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(widget = forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Your Full name Please'
    }))
    email = forms.EmailField(widget = forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Type your Email here'
    }))
    content = forms.CharField(widget = forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Your content'
    }))


class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your name here'
    }))
    
    password = forms.CharField(widget = forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':"Enter password here"
    }))


class RegisterForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={
    'class': 'form-control',
    'placeholder': 'Enter your name here'
}))

    email = forms.EmailField(widget = forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Type your Email here'
    }))

    password = forms.CharField(widget = forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':"Enter password here"
    }))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':"Re-Enter password here"
    }))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists(): 
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists(): 
            raise forms.ValidationError("Email is taken")
        return email



    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Password must match")
        return data
