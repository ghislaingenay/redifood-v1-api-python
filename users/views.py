from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from serializers import UserSerializer
from .models import User
from .password_manager import PasswordManager
import jwt, datetime
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
      email = request.data.get('email')
      password = request.data.get('password')
      user = User.objects.get(email=email)
      if User is None:
        raise AuthenticationFailed('Invalid credentials')
      if not user.check_password(password):
        raise AuthenticationFailed('Invalid credentials')
      return PasswordManager().generate_token()
    

class CurrentUserView(APIView):
  # Need to create a decorator to check if user is logged in
  def get(self, request):
    token = request.COOKIES.get('jwt')
    payload = PasswordManager().verify_token(token)
    user = User.objects.filter(id=payload['id'])
    serializer= UserSerializer(user)
    return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
      response = Response()
      response.delete_cookie('jwt')
      response.data = { 'message': 'Success'}
      return response
    
