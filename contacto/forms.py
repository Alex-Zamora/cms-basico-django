from django import forms

class ContactForm(forms.Form):
	nombre = forms.CharField(max_length=255)
	telefono = forms.CharField(max_length=20)
	email = forms.EmailField(max_length=70)
	mensaje = forms.CharField()