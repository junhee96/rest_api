from django.db import models
from accounts.models import User
from product.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='사용자') 
    products = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='상품')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='주문날짜')
    quantity = models.IntegerField(verbose_name='수량')

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table='orders'
        verbose_name='주문'
        verbose_name_plural='주문'
