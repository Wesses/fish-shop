from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    description = models.TextField(null=True, blank=True)
    available = models.BooleanField(null=True)
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey('Order', null=True, on_delete=models.PROTECT, verbose_name='Заказ')

    def __str__(self):
        return f"Product - {self.title}"

class Order(models.Model):
    order_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
