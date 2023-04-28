from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import connection
from .serializers import OrderSerializer

# Create your views here.
class TestView(APIView):
  def get(self, request):
      return Response('Get Orders')
    
class OrdersView(APIView):
  # Get all or only paid orders
  def get(self, request):
    paid_orders_param = request.GET.get('paidOrders', False)
    build_sql_query = 'WHERE order_status = COMPLETED' if paid_orders_param == True else ''
    with connection.cursor() as cursor:
      cursor.execute('SELECT * FROM foods_food '+build_sql_query )
      rows = cursor.fetchall()
      return Response(rows)
  
  def post(self, request):
    serializer = OrderSerializer(data=request.data) 
    if serializer.is_valid():
      serializer.save()
      
class OrderView(APIView):
  # get one order
  # update only order
  # delete one order