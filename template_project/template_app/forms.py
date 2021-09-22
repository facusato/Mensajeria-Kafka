from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from . import models


class RegisterForm(UserCreationForm):
	username = forms.CharField(label='Usuario', widget = forms.TextInput(attrs={'placeholder':'Usuario'}), required = True)
	first_name = forms.CharField(label='Usuario', widget = forms.TextInput(attrs={'placeholder':'Nombre de Pila'}), required = True)
	password1 = forms.CharField(label='Password 1', help_text='La contraseña debe contener mas de 8 caracteres alfanumericos', widget=forms.PasswordInput(attrs={'placeholder':'Password 1'}), required = True)
	password2 = forms.CharField(label='Password 2', widget=forms.PasswordInput(attrs={'placeholder':'Password 2'}), required = True)


class LoginForm(forms.Form):
	username = forms.CharField(label='Usuario', widget = forms.TextInput(attrs={'placeholder':'Usuario'}), required = True)
	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Password'}), required = True)

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'password1', 'password2']

#class ModelForm(ModelForm):
#	class Meta:
#		model = models.model_name
#		fields = '__all__'
#		widgets = {
#			'username' : forms.TextInput(attrs = {'placeholder': 'Username'}),
#			'email' : forms.TextInput(attrs = {'placeholder': 'E-Mail'}),
#			'password': forms.PasswordInput(attrs = {'placeholder': 'Password'}), 
#			'password2': forms.PasswordInput(attrs = {'placeholder': 'Password repeat'}), 
#		}

#class NameForm(forms.Form):
#	field_name = forms.CharField(label='', widget = forms.TextInput(attrs={'placeholder':'Mensaje a Enviar'}), required = True)
	


class MessageForm(forms.Form):
	mensaje = forms.CharField(label='', widget = forms.TextInput(attrs={'placeholder':'Mensaje a Enviar'}), required = True)
	

class CargarPost(forms.Form):
	titulo = forms.CharField(label='Titulo', widget = forms.TextInput(attrs={'placeholder':'Titulo del Post'}), required = True)
	imagen = forms.FileField(label='Ingrese una imagen', required = False)
	texto = forms.CharField(label='Texto', widget = forms.Textarea(attrs={'placeholder':'Texto del Post'}), required = True)
	


class BuscarUsrForm(forms.Form):
	mensaje = forms.ModelChoiceField(queryset=User.objects.all())


class ObtenerPost(forms.Form):
	autor = forms.CharField(widget = forms.HiddenInput(), required = True)
	titulo = forms.CharField(widget = forms.HiddenInput(), required = True)
	texto = forms.CharField(widget = forms.HiddenInput(), required = True)
	
