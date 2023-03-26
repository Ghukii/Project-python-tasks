from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd 

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

def get_path_from_file():
    with open('Task 5/path.txt', 'r') as file:
        path = file.read()
    file.close()
    return path

Image_path = Label(
    frame,
    text = get_path_from_file(),
)
Image_path.grid(row=1, column=1)

def callback():
    path = fd.askopenfilename()
    with open('Task 5/path.txt', 'w') as file:
        file.write(path)
    file.close()
    print(path)


get_image_path = Button(
    frame,
    text='Открыть файл', 
    command=callback
)
get_image_path.grid(row=1, column=3)

window.mainloop()

