from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response

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