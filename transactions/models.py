from django.db import models
from products.models import Product
from core.models import CustomUser
from django.utils.timezone import datetime
from django.db.models import Sum, Count


class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sales_person = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                                     related_name="salesperson_transactions")
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                                 related_name="customer_transactions")
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-create_date",)

    def __str__(self):
        return self.product.display_name

    @staticmethod
    def get_today_sales_info():
        sale_info = Transaction.objects.filter(create_date__date=datetime.today()) \
            .aggregate(total_sale=Count('pk'), sales_amount=Sum('product__cost'))
        return sale_info
