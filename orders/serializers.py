from rest_framework import serializers
from .models import Order,  OrderItem

class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model=Order
    fields=['user', 'food', 'order_status', 'order_total']
  
  def validate(self, data):
    """
    Check that start is before finish.
    """
    if data['order_total'] <  0:
        raise serializers.ValidationError("Order amount must be positive")
    
    return data


class OrderItemSerializer(serializers.ModelSerializer):
  model=OrderItem
  fields='__all__'
  
