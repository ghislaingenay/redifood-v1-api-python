import jwt, datetime
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

class PasswordManager:
  token_expiration_time_min = 60
  basic_secret = 'secret'
  payload = None
  
  def __init__(self):
    pass
  
  def set_payload(self, user_id):
    self.payload = {'id': user_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=self.token_expiration_time_min), 'iat': datetime.datetime.utcnow()}
    
  def generate_token(self, user_id):
    self.set_payload(user_id)
    token = jwt.encode(self.payload, self.basic_secret, algorithm='HS256').decode('utf-8')
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    return response

  def verify_token(self, token):
    if not token:
      raise AuthenticationFailed('Unauthenticated')
    try:
      payload = jwt.decode(token, self.basic_secret, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
      raise AuthenticationFailed('Unauthenticated')
    except jwt.exceptions.DecodeError:
      raise AuthenticationFailed('Unauthenticated')
    return payload