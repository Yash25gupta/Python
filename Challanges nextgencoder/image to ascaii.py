from PIL import Image
import os

ASCII_CHARS = ('@', '#', '$', '%', '?', '*', '+', ';', ':', ',', '.')


def resize_image(image, new_width):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def grayify(image):
    grayscale_image = image.convert('L')
    return grayscale_image


def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = ''.join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters


def main(path, new_width=100):
    try:
        img = Image.open(path)
    except Exception:
        print(path, "is not a valid pathname to an image.")
        return 0

    new_image_data = pixel_to_ascii(grayify(resize_image(img, new_width)))

    pixel_count = len(new_image_data)
    ascii_img = '\n'.join(new_image_data[i:(i + new_width)]
                          for i in range(0, pixel_count, new_width))

    with open(path[:-4] + ' ascii.txt', 'w') as f:
        f.write(ascii_img)


# path = input('Enter a valid pathname to an image:\n')
# main(path, 120)
for pic in os.listdir('ME'):
    if pic.endswith('.jpg'):
        picPath = os.path.join('ME', pic)
        main(picPath, 40)
