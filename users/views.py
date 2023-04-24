from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
from .jwt_manager import JWTManager
from django.shortcuts import get_object_or_404
# Create your views here.

class RegisterView(APIView):
    def post(self, request):
      serializer = UserSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
        email = serializer.validated_data['email']
        serializer.save()
        user_id = self.get_user_id(email)
        print('usr', user_id)
        return JWTManager().generate_token(user_id,email)
        
    def get_user_id(self, email: str) -> int:
      try:
        print('email', email)
        user = get_object_or_404(User, email=email)
        print('recovered user')
        serializer = UserSerializer(user)
        return serializer.data['id']
      except User.DoesNotExist:
        raise AuthenticationFailed('User not found')
      

class LoginView(APIView):
    def post(self, request):
      email = request.data.get('email')
      password = request.data.get('password')
      user = User.objects.get(email=email)
      print('user', user)
      if User is None:
        raise AuthenticationFailed('Invalid credentials')
      if not user.check_password(password):
        raise AuthenticationFailed('Invalid credentials')
      return JWTManager().generate_token(user.id, email)
    

class CurrentUserView(APIView):
  # Need to create a decorator to check if user is logged in
  def get(self, request):
    token = request.COOKIES.get('jwt')
    payload = JWTManager().verify_token(token)
    user = User.objects.filter(id=payload['id'])
    serializer= UserSerializer(user)
    return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
      response = Response()
      response.delete_cookie('jwt')
      response.data = { 'message': 'Success'}
      return response
    

    