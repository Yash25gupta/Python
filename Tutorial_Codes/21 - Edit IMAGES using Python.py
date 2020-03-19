# installation of pillow library    --->    pip install Pillow
# change image extension                  # image
# resize image size                       # image
# resize multiple image using for loop    # image
# Sharpness                               # ImageEnhance
# Brightness                              # ImageEnhance
# Color                                   # ImageEnhance
# Contrast                                # ImageEnhance
# Image blur, GaussianBlur                # ImageFilter

from PIL import Image, ImageEnhance, ImageFilter
import os

img1 = Image.open('man.jpg')

# change extension
# img1.save('man.png')                
img1.save('man.pdf')
# img1.show()

# resize
max_size = (250,250)
img1.thumbnail(max_size)
img1.save('man_thumbnail.jpg')

for item in os.listdir():                   # change extension of all jpg file in a folder
    if item.endswith('.jpg'):
        img = Image.open(item)
        fname, ext = os.path.splitext(item)
        img.save(f'{fname}.png')

# 0 : blury
# 1 : original
# 2+ : image with increased sharpness

sharpen = ImageEnhance.Sharpness(img1)
sharpen.enhance(3).save('mansharpness.jpg')

colorify = ImageEnhance.Color(img1)
colorify.enhance(3).save('mancolor.jpg')

bright = ImageEnhance.Brightness(img1)
bright.enhance(3).save('manbrightness.jpg')

contrast = ImageEnhance.Contrast(img1)
contrast.enhance(3).save('mancontrast.jpg')

img1.filter(ImageFilter.GaussianBlur(radius=4)).save('manblur.jpg')

