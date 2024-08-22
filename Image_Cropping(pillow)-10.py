from PIL import Image

image_open = Image.open('E:\python-images\image4.jpg')

image_crop = image_open.crop((100, 50, 400, 300))

image_crop.show()