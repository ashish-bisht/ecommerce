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
