from django.db import models

# Create your models here.
class Order(models.Model):
  ORDER_STATUS = [
    ("CREATED", "CREATED"),
    ("UPDATED", "UPDATED"),
    ("AWAIT_PAYMENT", "AWAIT_PAYMENT"),
    ("COMPLETED", "COMPLETED"),
]
  user = models.ForeignKey('users.User', on_delete=models.CASCADE)
  food = models.ForeignKey('foods.Food', on_delete=models.CASCADE)
  order_status= models.CharField(max_length=20, choices=ORDER_STATUS, default="CREATED")
  order_total = models.FloatField(max_length=20, default=0)
  order_created_at = models.DateTimeField(auto_now_add=True)
  order_updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f'{self.user} - {self.food} - {self.quantity}'


class OrderItem(models.Model):
  order = models.ForeignKey('Order', on_delete=models.CASCADE)
  food = models.ForeignKey('foods.Food', on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)
  
  def __str__(self):
    return self.food.food_name[:50]