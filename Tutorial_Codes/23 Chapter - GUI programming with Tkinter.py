# Tutorial 232 - Tkinter[1] Create GUI App with Python
# tee-kinter, tk-inter, kinter

# starter code
# import tkinter
# win = tkinter.Tk()      # mostly used variable --> root, win, window

# from tkinter import *
# win = Tk()

from csv import DictWriter
import os
import tkinter as tk
from tkinter import ttk         # buttons, ... are good in view
win = tk.Tk()      # mostly used variable --> root, win, window
win.title('GUI')

# Create lables
# widgets -->  lables, buttons, radio button - tk, ttk
name_lable = ttk.Label(win, text='Enter your name : ')
name_lable.grid(row=0, column=0, sticky=tk.W)                        # pack, grid

email_lable = ttk.Label(win, text='Enter your email : ')
email_lable.grid(row=1, column=0, sticky=tk.W)

age_lable = ttk.Label(win, text='Enter your age : ')
age_lable.grid(row=2, column=0, sticky=tk.W)

gender_lable = ttk.Label(win, text='Select your gender : ')
gender_lable.grid(row=3, column=0, sticky=tk.W)

# Create entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width=16, textvariable=name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win, width=16, textvariable=email_var)
email_entrybox.grid(row=1, column=1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win, width=16, textvariable=age_var)
age_entrybox.grid(row=2, column=1)

# Combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=14, textvariable=gender_var, state='readonly')
gender_combobox['values'] = ('Male', 'Female', 'Other')
gender_combobox.current(0)
gender_combobox.grid(row=3, column=1)

# Radio buttton
# Eg - student, teacher
usertype = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win, text='Student', value='Student', variable=usertype)
radiobtn1.grid(row=4, column=0)

radiobtn2 = ttk.Radiobutton(win, text='Teacher', value='Teacher', variable=usertype)
radiobtn2.grid(row=4, column=1)

# check button
checkbtn_var = tk.IntVar()
checkbtn1 = ttk.Checkbutton(win, text='Chech if you want to suscribe', variable=checkbtn_var)
checkbtn1.grid(row=5, columnspan=3)

# Create a button
def action():
    username = name_var.get()
    useremail = email_var.get()
    userage = age_var.get()
    usergender = gender_var.get()
    user_type = usertype.get()
    if checkbtn_var.get() == 0:
        suscribed = 'NO'
    else:
        suscribed = 'YES'

    # #  Write in TXT file
    # with open('file.txt', 'a') as f:
    #     f.write(f'{username},{useremail},{userage},{usergender},{user_type},{suscribed}\n')

    # Write in CSV file
    with open('file.csv', 'a', newline='') as f:
        dict_writer = DictWriter(f, fieldnames=['UserName', 'UserEmail', 'UserAge', 'UserGender', 'UserType', 'Suscribed'])
        if os.stat('file.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'UserName' : username,
            'UserEmail' : useremail,
            'UserAge' : userage,
            'UserGender' : usergender,
            'UserType' : user_type,
            'Suscribed' : suscribed
        })

    name_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)

    name_lable.configure(foreground='#b388ff')
    # submit_button.configure(foreground='Blue')  # btn foreground color work with 'tk'


submit_button = tk.Button(win, text='Submit', command=action)
submit_button.grid(row=6, column=0)


win.mainloop()          # prevent window to close


# *****************************************************************************************
# Tutorial 233 - Tkinter[2] (Python GUI) Create Widgets using loop
# Tutorial 234 - Tkinter[3] (Python GUI) Padding
# for loop
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('LOOP')

# Labels
labels = ['What is your name : ', 'What is your age : ', 'What is your gender : ', 'Country : ', 'State : ', 'City : ']
for i in range(len(labels)):
    cur_label = 'label' + str(i)    # lable0, lable1,...
    cur_label = ttk.Label(win, text= labels[i])
    cur_label.grid(row=i, column=0, sticky=tk.W, padx= 2, pady=2)

# Entry box
user_info ={
    'name': tk.StringVar(),
    'age': tk.StringVar(),
    'gender': tk.StringVar(),
    'Country': tk.StringVar(),
    'State': tk.StringVar(),
    'City': tk.StringVar()
}
counter = 0
for i in user_info:
    cur_entrybox = 'entry' + i    # entryname, entryage,...
    cur_entrybox = ttk.Entry(win, width=16, textvariable=user_info[i])
    cur_entrybox.grid(row=counter, column=1, padx= 2, pady=2)
    counter += 1

# Submmit Btn
def submit():
    print(user_info['name'].get())
    print(user_info['age'].get())
    print(user_info['gender'].get())
    print(user_info['Country'].get())
    print(user_info['State'].get())
    print(user_info['City'].get())
    
submit_btn = ttk.Button(win, text='Submit', command=submit)
submit_btn.grid(row=6, columnspan=2)

win.mainloop()


# *****************************************************************************************
# Tutorial 234 - Tkinter[3] (Python GUI) LabelFrame
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('Label Frame')

# Label Frame
label_frame = ttk.LabelFrame(win, text='Enter your details below')
label_frame.grid(row=0, column=0, padx=10, pady=10)

# Labels
labels = ['What is your name : ', 'What is your age : ', 'What is your gender : ', 'Country : ', 'State : ', 'City : ']
for i in range(len(labels)):
    cur_label = 'label' + str(i)    # lable0, lable1,...
    cur_label = ttk.Label(label_frame, text= labels[i])
    cur_label.grid(row=i, column=0, sticky=tk.W)

# Entry box
user_info ={
    'name': tk.StringVar(),
    'age': tk.StringVar(),
    'gender': tk.StringVar(),
    'Country': tk.StringVar(),
    'State': tk.StringVar(),
    'City': tk.StringVar()
}
counter = 0
for i in user_info:
    cur_entrybox = 'entry' + i    # entryname, entryage,...
    cur_entrybox = ttk.Entry(label_frame, width=16, textvariable=user_info[i])
    cur_entrybox.grid(row=counter, column=1)
    counter += 1

# Submmit Btn
def submit():
    print(user_info['name'].get())
    print(user_info['age'].get())
    print(user_info['gender'].get())
    print(user_info['Country'].get())
    print(user_info['State'].get())
    print(user_info['City'].get())
    
submit_btn = ttk.Button(win, text='Submit', command=submit)
submit_btn.grid(row=1, columnspan=2)

for child in label_frame.winfo_children():
    child.grid_configure(padx=4, pady=4)

win.mainloop()


# *****************************************************************************************
# Tutorial 235 - Tkinter[4] Tabbed Control Widget
# notebook -- contain two pages
# page 1                                Page 2
# widgets                               widgets
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('TAB Control')

nb = ttk.Notebook(win)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
nb.add(page1, text='ONE')
nb.add(page2, text='TWO')
# nb.grid(row=0, column=0)
nb.pack(expand=True, fill='both')

lable1 =ttk.Label(page1, text='This is label : ')
lable1.grid(row=0, column=0)

lable2 =ttk.Label(page2, text='This is label : ')
lable2.grid(row=0, column=0)

entry1 = ttk.Entry(page1, width=26)
entry1.grid(row=0, column=1)

win.mainloop()


# *****************************************************************************************
# Tutorial 236 - Tkinter[5] Create Menubar
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('TAB Control')

def func():
    print('func called')

# Menu

# *****************************Simple Menubar*********************
# menubar = tk.Menu(win)
# menubar.add_command(label='Save', command=func)
# menubar.add_command(label='Save As', command=func)
# menubar.add_command(label='Copy', command=func)
# menubar.add_command(label='Paste', command=func)

main_menu = tk.Menu(win)

file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label='New File', command=func)
file_menu.add_command(label='New Window', command=func)
file_menu.add_separator()
file_menu.add_command(label='Save File', command=func)
file_menu.add_command(label='Save as', command=func)

edit_menu = tk.Menu(main_menu, tearoff=0)
edit_menu.add_command(label='Undo', command=func)
edit_menu.add_command(label='Redo', command=func)
edit_menu.add_command(label='Find', command=func)

main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='Edit', menu=edit_menu)

win.config(menu=main_menu)     # in case of menubar. (dont use grid,pack)

win.mainloop()


# *****************************************************************************************
# Tutorial 237 - Tkinter[6] Message Box and Exception handling
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box

win = tk.Tk()

# label frame
label_frame = ttk.LabelFrame(win, text='Contact Detail')
label_frame.grid(row=0, column=0, padx=40, pady=10)

# lables
name_label = ttk.Label(label_frame, text='Enter your Name please : ', font=('Helvetica', 12, 'bold'))
age_label = ttk.Label(label_frame, text='Enter your Age please : ', font=('Helvetica', 12, 'bold'))

# entry box variable
name_var = tk.StringVar()
age_var = tk.StringVar()

# entry box
name_entry = ttk.Entry(label_frame, width=36, textvariable=name_var)
age_entry = ttk.Entry(label_frame, width=36, textvariable=age_var)

# grid
name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
age_label.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
name_entry.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
age_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)


def submit():
    # m_box.showinfo('title', 'Content of this msg box !!')
    name = name_var.get()
    age = age_var.get()
    if name=='' or age=='':
        m_box.showerror('Error', 'Please fill both name and age.')
    else:
        try:
            age = int(age)
        except ValueError:
            m_box.showerror('Age Error', 'Only digits are allowed in age field.')
        else:
            if age < 18:
                m_box.showwarning('warning', 'you are below 18')
            print(f'{name} {age}')

submit_btn = ttk.Button(win, text='Submit', command=submit)
submit_btn.grid(row=1, columnspan=2, padx=40)

win.mainloop()

