from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  full_name = models.CharField(max_length=40, null=True)
  email = models.EmailField(max_length=254, unique=True)
  username = models.CharField(max_length=40, unique=True, null=True)
  password = models.CharField(max_length=40)
  created_at = models.DateTimeField(auto_now_add=True)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  
  
