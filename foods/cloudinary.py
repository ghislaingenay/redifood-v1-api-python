import base64
from django.core.files.base import ContentFile

class Cloudinary:
  

  def decode_base64_image(data: str) -> ContentFile:
    '''
    Function that decodes a base64 image and returns a ContentFile object which can be saved to a cloud provider
    '''
    format, imgstr = data.split(';base64,') 
    ext = format.split('/')[-1] 
    data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext) 

  def save_image_to_cloudinary(data: str) -> str:
    '''
    Function that saves an image to a cloud provider
    '''
    pass