from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['product', 'sales_person', 'customer']


admin.site.register(Transaction, TransactionAdmin)
