from users.jwt_manager import JWTManager
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

def is_authenticated(func):
  def middleware(self, request):
    jwt_token = request.COOKIES['jwt']
    payload = JWTManager().verify_token(jwt_token)
    yield payload
  return middleware

class AuthenticationMiddleware:
  def __init__(self, func):
    self.func = func

  def __call__(self, request):
    response = self.func(request)
    return response

  def process_view(self, request, view_func, view_args, view_kwargs):
    auth_list = ['login', 'register', 'logout']
    if view_func.__name__ not in auth_list:
      print('user', request.user)
      jwt_token = request.COOKIES['jwt']
      payload = JWTManager().verify_token(jwt_token)
      print('payload', payload)
      request.user = payload
      return view_func(request)
    else:
      return view_func(request)
    
  def process_exception(self, request, exception):
    raise AuthenticationFailed('Unauthenticated')