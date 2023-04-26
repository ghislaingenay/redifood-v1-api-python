from rest_framework import serializers

from foods.cloudinary import Cloudinary
from .models import Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
    
    def create(self, validated_data):
        base64_image = validated_data.get('image_url')
        new_url = Cloudinary.save_image_to_cloudinary(base64_image)
        validated_data['photo_url'] = new_url['secure_url']
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
        
    def update(self, instance, validated_data):
        food = Food.objects.get(id=instance.id)
        if food.base64_image != validated_data.get('base64_image'):
            base64_image = validated_data.get('base64_image')
            new_url = Cloudinary.save_image_to_cloudinary(base64_image)
            validated_data['photo_url'] = new_url['secure_url']
        return super(FoodSerializer, self).update(instance, validated_data)
    