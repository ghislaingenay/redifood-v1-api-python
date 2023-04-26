from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from operator import itemgetter
from foods.cloudinary import Cloudinary

from foods.serializer import FoodSerializer

# Create your views here. 
class GetFoodsView(APIView):
  def get(self, request):
    print('user', request.user)
    with connection.cursor() as cursor:
      cursor.execute('SELECT * FROM foods_food')
      rows = cursor.fetchall()
      return Response(rows)
    
    
class FoodIdView(APIView):
  def get(self, request, food_id):
    with connection.cursor() as cursor:
      cursor.execute(f'SELECT * FROM foods_food WHERE id = {food_id}')
      rows = cursor.fetchall()
      return Response(rows)
    
  def delete(self, request, food_id):
    with connection.cursor() as cursor:
      cursor.execute(f'DELETE FROM foods_food WHERE id = {food_id}')
      return Response({'message': 'Food deleted'})
  
  def put(self, request, food_id):
    serializer = FoodSerializer(data=request.data)
    if serializer.is_valid():    
      food_name, food_description, food_price, image_url, food_category = itemgetter('food_name', 'food_description', 'food_price', 'image_url', 'food_category', 'base64_image')(serializer.validated_data)
      with connection.cursor() as cursor:
        cursor.execute(f'UPDATE foods_food SET food_name = "{food_name}", food_description = "{food_description}", food_price = {food_price}, image_url = "{image_url}", food_category = "{food_category}", base64_image="{base64_image}" WHERE id = {food_id}')
        return Response({'message': 'Food updated'})
      
  def post(self, request):
    serializer = FoodSerializer(data=request.data) # Create in FoodSerializer create a url link directly
    if serializer.is_valid():
      serializer.save()
    