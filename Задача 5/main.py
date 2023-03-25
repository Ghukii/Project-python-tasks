from PIL import Image
import numpy as np

img = Image.open("C:/Users/Admin/Documents/GitHub/Project-python-tasks/Задача 5/Image.png")

print("Введите фразу для шифрования:")
phrase = list(input())
print(phrase)

obj = img.load()
(weight, height) = img.size

def code_letter_in_pixel(pixel, letter):
    new_pixel = list()
    delta1, delta2 = ord(letter) // 3, ord(letter) // 3
    delta3 = ord(letter) - delta1 - delta2
    if pixel[0] >= 127:
        new_pixel.append(pixel[0] - delta1)
    else:
        new_pixel.append(pixel[0] - delta1)
    if pixel[0] >= 127:
        new_pixel.append(pixel[1] - delta2)
    else:
        new_pixel.append(pixel[1] - delta2)
    if pixel[0] >= 127:
        new_pixel.append(pixel[2] - delta3)
    else:
        new_pixel.append(pixel[2] - delta3)
    return tuple(new_pixel)

i = 0
j = 0
while phrase:
    letter = phrase.pop(0)
    img.putpixel((i, j), code_letter_in_pixel(img.getpixel((i, j)), letter))
    j += 1
    if j > weight:
        i += 1
        j = 0

img.save("coded_inage.png")

