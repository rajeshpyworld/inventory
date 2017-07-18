from django import forms
from .models import Transaction
from core.models import CustomUser
from products.models import Product


class TransactionForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control'}))

    sales_person = forms.ModelChoiceField(queryset=CustomUser.salespersons.all(),
                                          widget=forms.Select(attrs={'class': 'form-control'}))

    customer = forms.ModelChoiceField(queryset=CustomUser.customers.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Transaction
        fields = ['product', 'sales_person', 'customer']
