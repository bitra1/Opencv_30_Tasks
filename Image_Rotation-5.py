from PIL import Image

img = Image.open('E:\python-images\image5.jpg')

if img is None:
    print('Check Source path of image')

else:
    rotated_image_45 = img.rotate(angle=45 ,expand=True)
    # rotated_image_90 = img.rotate(angle=90, expand=True)
    # rotated_image_180 = img.rotate(angle=180, expand=True)
    # rotated_image_360 = img.rotate(angle=360, expand=True)
    rotated_image_45.show(title='Angle')
    # rotated_image_90.show()
    # rotated_image_180.show()
    # rotated_image_360.show()
