from PIL import Image
import os

print(os.getcwd())

mac = Image.open(os.getcwd()+'/example.jpg')

print(type(mac))



mac.show()