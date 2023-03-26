from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd 
from main import *


window = Tk()
window.title("Стеганографическое приложение")
window.geometry("1024x1024")
frame = Frame(
   window, 
   padx = 10, 
   pady = 10 
)
frame.pack(expand=True)

Image_path_ask = Label(
    frame,
    text = 'Укажите путь к изображению:',
)
Image_path_ask.grid(row=1, column=1)

def callback():
    path = fd.askopenfilename()
    print(path)
    with open("Task 5/path.txt", 'w') as file:
        file.write(path)
    file.close()
    Image_path = Label(
    frame,
    text = path
    )
    Image_path.grid(row=1, column=2)


get_image_path = Button(
    frame,
    text='Открыть файл', 
    command=callback
)
get_image_path.grid(row=1, column=3)

space = Label(
    frame,
    text='                                                      '
)
space.grid(row=2,column=2)
space.grid(row=3,column=2)

get_phrase_ask = Label(
    frame,
    text="Введите текст который хотите зашифровать:"
)
get_phrase_ask.grid(row=4,column=1)

get_phrase = Entry(
    frame,
    width=70
)
get_phrase.grid(row=4, column=2)

def write_phrase_in_file():
    phrase = get_phrase.get()
    with open("Task 5/phrase.txt", 'w') as file:
        file.write(phrase)
    file.close()

def read_phrase_in_file():
    with open("Task 5/phrase.txt", 'r') as file:
        phrase = file.read()
    file.close()
    return phrase

enter_button = Button(
    frame,
    text = 'Подтвердить',
    command=write_phrase_in_file
)
enter_button.grid(row=4, column=3)

space.grid(row=6)
space.grid(row=7)

def get_path_from_file():
    with open("Task 5/path.txt", 'r') as file:
        path = file.read()
    file.close()
    return path

def zashifrovat():
    path = get_path_from_file()
    phrase = str(read_phrase_in_file())
    img = get_image(path)
    phrase = phrase_mod(phrase)
    delta = get_delta(phrase)
    res = shifr(img, delta)
    save_img(res)

zashifrovat_button = Button(
    frame,
    text="Зашифровать",
    command=zashifrovat
)
zashifrovat_button.grid(row=8, column=2)
window.mainloop()

