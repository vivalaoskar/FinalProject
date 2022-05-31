import tkinter as tk
import tkinter.filedialog as tk_file
from PIL import Image, ImageTk
from setuptools import Command 

root = tk.Tk()
root.geometry('800x600')
root.config(bg='black')

opened_image = ''
image_path = ''

edited_image = ''

image_height = 0
image_width = 0

def crop_image(left, top, right, bottom):
    global edited_image, opened_image

    edited_img = Image.open(image_path)
    edited_image = edited_img.crop((left, top, image_width - right, image_height - bottom))

    opened_image = ImageTk.PhotoImage(edited_image)

    image_lb.config(image=opened_image)


def clear_image():
    global opened_image, image_path, image_height, image_width

    opened_image = ''
    image_path = ''
    image_height = 0
    image_width = 0

def open_window():
    global opened_image, image_path, image_height, image_width

    image_path = tk_file.askopenfilename()
    if image_path:
        opened_image = ImageTk.PhotoImage(Image.open(image_path))
        image_lb.config(image=opened_image)

        image_height = opened_image.height()
        image_width = opened_image.width()

def save_image():
    if image_path:
        file_name = tk_file.asksaveasfilename()

        if file_name:
            edited_image.save(file_name)

def contols_window(w, h):
    controls = tk.Toplevel(root)
    controls.geometry('400x300')
    left_lb = tk.Label(controls, text='Left')
    left_lb.pack(anchor=tk.W, pady=5)

    left_scale = tk.Label(controls, from_=0, to=w, orient=tk.HORIZONTAL, 
                          Command=lambda x: crop_image(left_scale.get(),
                                                       top_scale.get(),
                                                       top_scale.get(),
                                                       right_scale.get(),
                                                       bottom_scale.get()))
    left_scale.pack(anchor=tk.W, fill=tk.X)

    right_lb = tk.Label(controls, text='Right')
    right_lb.pack(anchor=tk.W, pady=5)

    right_scale = tk.Scale(controls, from_=0, to=w, orient=tk.HORIZONTAL,  
                           Command=lambda x: crop_image(left_scale.get(),
                                                        top_scale.get(),
                                                        top_scale.get(),
                                                        right_scale.get(),
                                                        bottom_scale.get()))
    right_scale.pack(anchor=tk.W, fill=tk.X)

    top_lb = tk.Label(controls, text='Top')
    top_lb.pack(anchor=tk.W, pady=5, fill=tk.X)

    top_scale = tk.Scale(controls, from_=0, to=h, orient=tk.HORIZONTAL,  
                         Command=lambda x: crop_image(left_scale.get(),
                                                      top_scale.get(),
                                                      top_scale.get(),
                                                      right_scale.get(),
                                                      bottom_scale.get()))
    top_scale.pack(anchor=tk.W)

    bottom_lb = tk.Label(controls, text='Top')
    bottom_lb.pack(anchor=tk.W, pady=5, fill=tk.X)

    bottom_scale = tk.Scale(controls, from_=0, to=h, orient=tk.HORIZONTAL,  
                            Command=lambda x: crop_image(left_scale.get(),
                                                         top_scale.get(),
                                                         top_scale.get(),
                                                         right_scale.get(),
                                                         bottom_scale.get()))
    bottom_scale.pack(anchor=tk.W, fill=tk.X)



    controls.mainloop()


menu_bar = tk.Menu(root)
menu_bar.add_command(label='Open', command=opened_image)
menu_bar.add_command(label='Controls', command=lambda: contols_window(w = image_width,
                                                                      h = image_height))
menu_bar.add_command(label='Save')
menu_bar.add_command(label='Clear')

root.config(menu=menu_bar)

image_lb = tk.Label(root, bg='gray')
image_lb.pack(fill=tk.BOTH)
