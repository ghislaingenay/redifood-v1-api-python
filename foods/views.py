from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from users.auth_decorators import is_authenticated

# Create your views here. 
class GetFoodsView(APIView):
  def get(self, request):
    print('user', request.user)
    with connection.cursor() as cursor:
      cursor.execute('SELECT * FROM foods_food')
      rows = cursor.fetchall()
      return Response(rows)