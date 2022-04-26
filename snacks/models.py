from django.db import models

class Snack(models.Model):
    snack_name = models.CharField(max_length=50)
    snack_brand = models.CharField(max_length=100)
    snack_price = models.IntegerField(default=0)
    snack_producer = models.CharField(max_length=100)
    snack_stock_unit = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField(default=0)

    def status(self):
        if self.quantity > 1:
            return 'Available'
        else:
            return 'Reorder'