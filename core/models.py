from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class SalespersonManager(models.Manager):
    def get_queryset(self):
        return super(SalespersonManager, self).get_queryset().filter(user_type='S')


class CustomerManager(models.Manager):
    def get_queryset(self):
        return super(CustomerManager, self).get_queryset().filter(user_type='C')


class CustomUser(AbstractUser):
    type_choices = (
        ('S', 'salesperson'),
        ('C', 'customer'),
    )
    user_type = models.CharField(max_length=2,
                                 choices=type_choices,
                                 default='S')

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-date_joined']

    objects = UserManager()
    salespersons = SalespersonManager()
    customers = CustomerManager()

    @property
    def is_customer(self):
        if self.user_type == 'C':
            return True
        return False

    @property
    def is_salesperson(self):
        if self.user_type == 'S':
            return True
        return False
