from django import forms
from .models import Dress

class DressForm(forms.ModelForm):
    class Meta:
        model = Dress
        fields = ['dress_name', 'size', 'colour', 'price']
        widgets = {
            'dress_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_dress_name'}),
            'size': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_size'}),
            'colour': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_colour'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_price'}),
        }