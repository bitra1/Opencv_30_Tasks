#pip install pillow
from PIL import  Image

img = Image.open(r'E:\python-images\10mm.png')

image_resize = (400 ,400)

image = img.resize(image_resize)

image.save(r'E:\python-images\10m2.png')

image.show()