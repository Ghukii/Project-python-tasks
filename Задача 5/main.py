from PIL import Image
import numpy as np

img = Image.open("C:/Users/Admin/Documents/GitHub/Project-python-tasks/Задача 5/Image.png")

print("Введите фразу для шифрования:")
phrase = list(map(lambda x: bin(ord(x))[2:], input()))

def parameter(x):
    if len(x) < 8:
        print(x)
        x = ('0' * (8 - len(x))) + x
        print(x)
    return x

phrase = list(map(lambda x: parameter(x), phrase))

print(phrase)
delta = list()
for i in phrase:
    for j in range(0, len(i)-2, 2):
        delta.append(i[j] + i[j + 1])

def rgb_to_hex(r, g, b):
    return ('{:x}{:x}{:x}').format(r, g, b)

def hex_to_rgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in (2, 4, 6))

def shifr(delta):
    width, height = img.size
    x = 0
    y = 0
    while delta:
        d = delta.pop(0)
        r, g, b = img.getpixel((x, y))
    
        hexx = hex_to_rgb(hex(int(rgb_to_hex(r, g, b), 16) + int(d, 2)))
        img.putpixel((x, y), hexx)
        x += 1
        if x > width:
            x = 0
            y += 1
    return img

def save_img(img):
    img.save(f"coded_{img.name}.png")


