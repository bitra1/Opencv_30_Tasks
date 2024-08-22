# from imgaug import augmenters as iaa
# import imageio.v2 as imageio
# from matplotlib import pyplot as plt
#
# image =imageio.imread('E:\python-images\image6.jpg')
#
# aug_seq = iaa.Sequential([
#     iaa.Rotate((-45,45)),
#     iaa.Fliplr((0.5)),
#     iaa.Flipud((0.5)),
#     iaa.ScaleX((0.8,1.2)),
#     iaa.ScaleY((0.8,1.2))
# ])
#
# augmented_image = [ aug_seq(image=image)    for i in aug_seq]
#
# plt.figure(figsize=(15,10))
# plt.subplot(2,3,1)
# plt.imshow(image)
# plt.title('Orginal_Image')
# plt.axis('off')
#
# for i , aug_image in enumerate(augmented_image):
#     plt.subplot(2,3,i+2)
#     plt.imshow(aug_image)
#     plt.title(f'Augmented Image{ i+1}')
#     plt.axis('off')
#
# plt.tight_layout()
# plt.show()


from imgaug import augmenters as iaa
from imageio import v2 as imageio
from matplotlib import pyplot as plt

image = imageio.imread('E:\python-images\image6.jpg')


aug_seq = iaa.Sequential([
    iaa.Rotate((-45,45)),
    iaa.Fliplr((0.5)),
    iaa.Flipud((0.5)),
    iaa.ScaleX((0.8,1.2)),
    iaa.ScaleY((0.8,1.2))
])

augmented_images = [ aug_seq(image = image) for i in aug_seq]


plt.figure(figsize=(15,10))
plt.subplot(2,3,1)
plt.imshow(image)
plt.title('Orginal_Image')
plt.axis('off')

for i,aug_images in enumerate(augmented_images):
    plt.subplot(2,3,i+2)
    plt.imshow(aug_images)
    plt.title(f'Augmented_images{i+1}')
    plt.axis('off')

plt.tight_layout()
plt.show()

















