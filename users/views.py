from rest_framework.views import APIView
from rest_framework.response import Response
from serializers import UserSerializer
# Create your views here.

class RegisterView(APIView):
    def post(self, request):
      # Add validations system
      # Add JWT token system
      serializer = UserSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
      

class LoginView(APIView):
    def post(self, request):
      pass
    
class LogoutView(APIView):
    def post(self, request):
      pass
    
class CurrentUserView(APIView):
  login_required = True
  # Need to create a decorator to check if user is logged in
  def get(self, request):
    pass
