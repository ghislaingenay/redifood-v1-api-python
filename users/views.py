from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class RegisterView(APIView):
    def post(self, request):
      pass

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
