from PIL import Image
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox

win = tk.Tk()
win.title('Image Extension Changer')

# label frame
label_frame = ttk.LabelFrame(win, text='Extensions')
label_frame.grid(row=0, column=0, padx=40, pady=10)

# lables
path_label = ttk.Label(label_frame, text='Enter your image Path : ', font=('Helvetica', 12, 'bold'))
extension_label = ttk.Label(label_frame, text='Final Extension : ', font=('Helvetica', 12, 'bold'))

# entry box variable
path_var = tk.StringVar()
extension_var = tk.StringVar()

# entry box
path_entry = ttk.Entry(label_frame, width=36, textvariable=path_var)
extension_entry = ttk.Entry(label_frame, width=16, textvariable=extension_var)

# grid
path_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
extension_label.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
path_entry.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
extension_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

def convertimg():
    path = path_var.get()
    extension = extension_var.get()
    if path=='' or extension=='':
        mbox.showerror('Error', 'Please fill both path and extension.')
    else:
        if '.' in extension:
            extension = extension[1:]
        if '.jpg' in path:
            img = Image.open(path)
            img.save(path[:-3] + extension)
            mbox.showinfo('Done', f'Your image is converted to {extension} format')
        else:
            mbox.showerror('Error', 'Please select "JPG" image')
    
submit_btn = ttk.Button(win, text='Convert', command=convertimg)
submit_btn.grid(row=1, columnspan=2, padx=40)


win.mainloop()