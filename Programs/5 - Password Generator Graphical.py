from random import choice, sample
import tkinter as tk
from tkinter import ttk, messagebox as m_box
mix = number = symbol = l = None

lowers = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
uppers = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
nums = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
symbols = ("@", "#", "$", "%", "+", "\"", "/", "'", "!", "^", "?", ":", ".", "(", ")", "{", "}", "[", "]", "~", "-", "_", "=")

win = tk.Tk()
win.title('Password Generator')
win.geometry('480x260')

def bindfunc(event):
    makepassword()

def get_vars():
    global mix, number, symbol, l
    mix = want_mixcase_var.get()
    number = want_num_var.get()
    symbol = want_symbol_var.get()
    try:
        l = int(length_entry_var.get())
        if l < 6 or l > 32:
            m_box.showwarning(
                'Warning', 'Password length should lie b/w "6-20".')
    except ValueError:
        m_box.showerror('Value Error', 'Please type digits only.')

def makepassword():
    password = ''
    count = 0
    get_vars()
    while count < l:
        password += choice(lowers)
        count += 1
        if number and count < l:    # Numbers
            password += choice(nums)
            count += 1
        if mix and count < l:       # Mixed Case
            password += choice(uppers)
            count += 1
        if symbol and count < l:    # Symbols
            password += choice(symbols)
            count += 1
        if count == l:
            password = ''.join(sample(password, l))
    pass_label.configure(text='Generated Password : ' + password)
    btn1.configure(text='Generate Password Again')

length_label = ttk.Label(win, text='Number of Character : ', font=('Helvetica', 12, 'bold'))
length_label.grid(row=0, column=0, sticky=tk.W, padx=20, pady=10)

length_entry_var = tk.StringVar()
length_entry = ttk.Entry(win, width=28, textvariable=length_entry_var)
length_entry.grid(row=0, column=1)
length_entry.bind('<Return>', bindfunc)
length_entry.focus()

want_num_var = tk.BooleanVar(value=1)
num = ttk.Checkbutton(win, text='Do you want Numbers in your Password.', variable=want_num_var)
num.grid(row=1, columnspan=2, padx=20, pady=10, sticky=tk.W)

want_mixcase_var = tk.BooleanVar(value=1)
case = ttk.Checkbutton(win, text='Do you want Mixed Case in your Password.', variable=want_mixcase_var)
case.grid(row=2, columnspan=2, padx=20, pady=10, sticky=tk.W)

want_symbol_var = tk.BooleanVar(value=1)
sym = ttk.Checkbutton(win, text='Do you want Symbols in your Password.', variable=want_symbol_var)
sym.grid(row=3, columnspan=2, padx=20, pady=10, sticky=tk.W)

btn1 = ttk.Button(win, text='Generate Password', command=makepassword)
btn1.grid(row=4, columnspan=2, pady=10)

pass_label = ttk.Label(win, text='', font=('Helvetica', 16, 'bold'))
pass_label.grid(row=5, columnspan=2, pady=10, sticky=tk.W)

win.mainloop()
