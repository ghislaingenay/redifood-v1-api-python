import base64
from django.core.files.base import ContentFile
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os

class Cloudinary:
  cloudinary.config( 
  cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME'),
  api_key = os.getenv('CLOUDINARY_API_KEY'), 
  api_secret = os.getenv('CLOUDINARY_API_SECRET'),
  secure = True
)
  

  def decode_base64_image(data: str) -> ContentFile:
    '''
    Function that decodes a base64 image and returns a ContentFile object which can be saved to a cloud provider
    '''
    format, imgstr = data.split(';base64,') 
    ext = format.split('/')[-1] 
    data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext) 

  def save_image_to_cloudinary(base64_file: str) -> str:
    '''
    Function that saves an image to a cloud provider
    '''
    created_file = cloudinary.uploader.upload(base64_file)
    return created_file