import email
from django import forms

class Forms_Contacto(forms.Form):
    name = forms.CharField(label="Nombre", required=True ,max_length=30)

    email = forms.CharField(label="Email", required=True ,max_length=30)

    contenido=forms.CharField(label="Contenido", widget=forms.Textarea)


    # your_name = forms.CharField(label='Your name', max_length=100)