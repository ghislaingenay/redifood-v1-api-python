from django.db import models

def 

# Create your models here.
class Food(models.Model):
    food_name = models.CharField(max_length=100,null=False, required=True)
    food_description = models.TextField(max_length=500, blank=True, required=False)
    food_price = models.DecimalField(max_digits=5, decimal_places=2)
    image_url = models.CharField(max_length=200, blank=True, required=False)
    food_category = models.CharField(max_length=100, blank=True, required=False)

    def __str__(self):
        return self.food_name[:50]
      
    