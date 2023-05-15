from django.db import models
from django.core.validators import RegexValidator
from myshop.models import Product


class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Номер телефону повинен бути введений в форматі: '+9999999999'. До 15 цифр доступно.")
    customer_phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    customer_email = models.EmailField()
    products = models.ManyToManyField(Product)
    date_created = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Order #{self.pk}'
