from django import forms
from django.forms import widgets, ModelChoiceField
from .models import information

class infoForm (forms.ModelForm):
    class Meta:
        model = information
        fields = [
            'dircopy',
            'dirsave',
            'sector',
            'maxsize',
            'nMax',
            'threads',
            'workers',
        ]
        widgets = {
            'username': forms.TextInput(attrs={ 'placeholder': 'Enter a username'}),
            'dircopy':  forms.TextInput(attrs={ 'placeholder': 'Enter directory to copy'}),
            'dirsave':  forms.TextInput(attrs={ 'placeholder': 'Enter directory to save'}),
            'sector':  forms.NumberInput(attrs={ 'placeholder': 'Enter number of sectors'}),
            'maxsize': forms.NumberInput(attrs={ 'placeholder': 'Enter max size per file'}),
            'nMax': forms.NumberInput(attrs={ 'placeholder': 'Enter number of iterations'}),
            'threads': forms.NumberInput(attrs={ 'placeholder': 'Enter number of threads'}),
            'workers': forms.NumberInput(attrs={ 'placeholder': 'Enter number of workers'}),
        }

        labels = {
            'dircopy': 'Directory to copy',
            'dirsave': 'Directory to save',
            'sector': 'Number of sectors',
            'maxsize': 'Max size of file',
            'nMax': 'Number of iterations',
            'threads': 'Number of threads',
            'workers': 'Number of workers',
        }