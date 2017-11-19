from django import forms

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