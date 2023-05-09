import io 
import os 

from google.cloud import vision
from google.oauth2 import service_account


# 身分証明書のjsonを読み込んでいる
# docker-compose.yamlで直接読み込ませることも可能
credentials = service_account.Credentials.from_service_account_file('key.json')
client=vision.ImageAnnotatorClient(credentials=credentials)

def text_detection(image):
  response=client.document_text_detection(image=image,image_context={'language_hints':['ja']})


image_name='text.webp'
filename=os.path.abspath('resources/'+image_name)

with io.open(filename,'rb') as image_file:
  content=image_file.read()

image=vision.Image(content=content)
text_detection(image)