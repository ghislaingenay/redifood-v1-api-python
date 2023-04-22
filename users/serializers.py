from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.User
    fields = ['id', 'email', 'full_name', 'password']
    extra_kwargs = {'password': {'write_only': True}} #Remove the password on the response after register a user
  
  def create(self, validated_data):
    password = validated_data.pop('password', None)
    instance = self.Meta.model(**validated_data)
    if password is not None:
      instance.set_password(password) 
    instance.save()
    return instance