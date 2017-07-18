from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    display_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=100,
        required=True)
    cost = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True)

    brand = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=100,
        required=True)

    class Meta:
        model = Product
        fields = ['display_name', 'cost', 'brand']
