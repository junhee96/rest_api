from django.db import models

 
class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    manufacturer = models.CharField(max_length=256, verbose_name='제조사')
    stock = models.IntegerField(verbose_name='재고')
    price = models.IntegerField(verbose_name='단가')
    shelf_life = models.DateField(blank=True, verbose_name='유통기한')

    def __str__(self):
        return self.name

    class Meta:
        db_table='products'
        verbose_name='상품'
        verbose_name_plural='상품'
