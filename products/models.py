from django.db import models


class Product(models.Model):
    display_name = models.CharField(max_length=120)
    cost = models.FloatField()
    brand = models.CharField(max_length=120)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-create_date",)

    def __str__(self):
        return self.display_name
