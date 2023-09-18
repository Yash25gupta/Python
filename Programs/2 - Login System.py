import os
from csv import DictReader, DictWriter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box

win = tk.Tk()
win.title('Login System')
default_frame = ttk.LabelFrame(win)
signup_frame = ttk.LabelFrame(win)
login_frame = ttk.LabelFrame(win)
forget_frame = ttk.LabelFrame(win)
default_frame.grid(row=0, column=0, padx=50, pady=20)
signup_frame.grid(row=0, column=0, padx=50, pady=20)
login_frame.grid(row=0, column=0, padx=50, pady=20)
forget_frame.grid(row=0, column=0, padx=50, pady=20)
signup_frame.grid_remove()
login_frame.grid_remove()
forget_frame.grid_remove()


def signup():
    default_frame.grid_remove()
    login_frame.grid_remove()
    forget_frame.grid_remove()
    signup_frame.grid()


def login():
    default_frame.grid_remove()
    signup_frame.grid_remove()
    forget_frame.grid_remove()
    login_frame.grid()
    l_entry_username.focus()


def forget():
    login_frame.grid_remove()
    forget_frame.grid()


# Default Page
d_label_1 = ttk.Label(default_frame, text='Welcome to this Login System', font=('Helvetica', 14, 'bold'))
d_label_1.grid(row=0, columnspan=5, pady=5)
d_label_2 = ttk.Label(default_frame, text='What do you want to do?', font=('Helvetica', 12, 'bold'))
d_label_2.grid(row=2, columnspan=5, pady=5)

d_btn_signup = ttk.Button(default_frame, text='Sign Up', command=signup)
d_btn_signup.grid(row=4, column=1)
d_btn_login = ttk.Button(default_frame, text='Login', command=login)
d_btn_login.grid(row=4, column=3)


# Signup Page
s_label_heading = ttk.Label(signup_frame, text='Fill up the given form', font=('Helvetica', 14, 'bold'))
s_label_heading.grid(row=0, columnspan=5)
s_labels = ('Enter your First Name : ', 'Enter your Last Name : ', 'Enter your D.O.B : ',
            'Create a Username : ', 'Create a Password : ', 'Reenter your Password : ')
for i in range(len(s_labels)):
    cur_label = 's_label' + str(i)
    cur_label = ttk.Label(signup_frame, text=s_labels[i])
    cur_label.grid(row=i + 2, column=0, sticky=tk.W, padx=2, pady=2, columnspan=2)

s_entry_var = {'firstname': tk.StringVar(), 'lastname': tk.StringVar(), 'dob': tk.StringVar(),
               'username': tk.StringVar(), 'password': tk.StringVar(), 'password2': tk.StringVar()}
s_entry = {}
counter = 2
for i in s_entry_var:
    s_entry[i] = ttk.Entry(signup_frame, width=28, textvariable=s_entry_var[i])
    s_entry[i].grid(row=counter, column=3, columnspan=2, padx=2, pady=2)
    counter += 1
s_entry['firstname'].focus()


def s_submit():
    s_user_firstname = s_entry_var['firstname'].get().title()
    s_user_lastname = s_entry_var['lastname'].get().title()
    s_user_dob = s_entry_var['dob'].get()
    s_user_username = s_entry_var['username'].get()
    s_user_password = s_entry_var['password'].get()
    s_user_password2 = s_entry_var['password2'].get()

    if s_user_firstname == '' or s_user_lastname == '' or s_user_dob == '' or s_user_username == '' or s_user_password == '' or s_user_password2 == '':
        m_box.showerror('Empty Box', 'Please fill all above entry box')
    elif s_user_password != s_user_password2:
        m_box.showerror('Incorret Password', 'Please type same password in both the box.')
    else:
        with open('Login_data.csv', 'r') as f:
            csv_reader = DictReader(f)
            for row in csv_reader:
                if s_user_username == row['Username']:
                    m_box.showerror('Username', 'Username not available')
                    return
        with open('Login_data.csv', 'a', newline='') as f:
            csv_writer = DictWriter(
                f, fieldnames=['First_Name', 'Last_Name', 'DOB', 'Username', 'Password'])
            if os.stat('Login_data.csv').st_size == 0:
                csv_writer.writeheader()
            csv_writer.writerow({
                'First_Name': s_user_firstname,
                'Last_Name': s_user_lastname,
                'DOB': s_user_dob,
                'Username': s_user_username,
                'Password': s_user_password
            })
        s_clearall()


def s_clearall():
    s_entry['firstname'].delete(0, tk.END)
    s_entry['lastname'].delete(0, tk.END)
    s_entry['dob'].delete(0, tk.END)
    s_entry['username'].delete(0, tk.END)
    s_entry['password'].delete(0, tk.END)
    s_entry['password2'].delete(0, tk.END)
    s_entry['firstname'].focus()


s_btn_submit = ttk.Button(signup_frame, text='Submit', command=s_submit)
s_btn_clear = ttk.Button(signup_frame, text='ReLoad', command=s_clearall)
s_btn_login = ttk.Button(signup_frame, text='Login', command=login)
s_btn_submit.grid(row=9, column=0)
s_btn_clear.grid(row=9, column=2)
s_btn_login.grid(row=9, column=4)


# Login Page
l_label_heading = ttk.Label(login_frame, text='Login using your Username and Password', font=('Helvetica', 14, 'bold'))
l_label_username = ttk.Label(login_frame, text='Enter your Username : ', font=('Helvetica', 12, 'bold'))
l_label_password = ttk.Label(login_frame, text='Enter your Password : ', font=('Helvetica', 12, 'bold'))
l_label_heading.grid(row=0, columnspan=5)
l_label_username.grid(row=2, column=0, columnspan=2, padx=2, pady=2, sticky=tk.W)
l_label_password.grid(row=3, column=0, columnspan=2, padx=2, pady=2, sticky=tk.W)

l_entry_var_username = tk.StringVar()
l_entry_var_password = tk.StringVar()

l_entry_username = ttk.Entry(login_frame, width=28, textvariable=l_entry_var_username)
l_entry_password = ttk.Entry(login_frame, width=28, textvariable=l_entry_var_password)
l_entry_username.focus()
l_entry_username.grid(row=2, column=3, columnspan=2, padx=2, pady=2)
l_entry_password.grid(row=3, column=3, columnspan=2, padx=2, pady=2)


def l_clearall():
    l_entry_username.delete(0, tk.END)
    l_entry_password.delete(0, tk.END)
    l_entry_username.focus()


def l_login():
    l_user_username = l_entry_var_username.get()
    l_user_password = l_entry_var_password.get()
    if l_user_username == '' or l_user_password == '':
        m_box.showerror('Empty Box', 'Please fill both box')
    else:
        with open('Login_data.csv', 'r') as f:
            csv_reader = DictReader(f)
            for row in csv_reader:
                if l_user_username == row['Username'] and l_user_password == row['Password']:
                    l_clearall()
                    msg = 'Hello ' + row['First_Name'] + ' ' + \
                        row['Last_Name'] + '. Your DOB is ' + row['DOB']
                    m_box.showinfo('Welcome', msg)
                    break
            else:
                m_box.showerror(
                    'Wrong Input', 'Entered Usernam or Password is wrong!!!')


l_btn_login = ttk.Button(login_frame, text='Log in', command=l_login)
l_btn_clear = ttk.Button(login_frame, text='Clear', command=l_clearall)
l_btn_forget_password = ttk.Button(login_frame, text='Forget Password', command=forget)
l_btn_signup = ttk.Button(login_frame, text='Sign Up', command=signup)
l_btn_login.grid(row=5, column=0, columnspan=2, sticky=tk.E, padx=2, pady=2)
l_btn_clear.grid(row=5, column=3, columnspan=2, sticky=tk.W, padx=2, pady=2)
l_btn_forget_password.grid(row=6, column=0, columnspan=2, sticky=tk.E, padx=2, pady=2)
l_btn_signup.grid(row=6, column=3, columnspan=2, sticky=tk.W, padx=2, pady=2)


# Forget page
f_label_heading = ttk.Label(forget_frame, text='Enter your Details', font=('Helvetica', 14, 'bold'))
f_label_name = ttk.Label(forget_frame, text='Enter your full name : ', font=('Helvetica', 10, 'bold'))
f_label_dob = ttk.Label(forget_frame, text='Enter your DOB : ', font=('Helvetica', 10, 'bold'))
f_label_heading.grid(row=0, columnspan=5)
f_label_name.grid(row=2, column=0, columnspan=2, padx=2, pady=2, sticky=tk.W)
f_label_dob.grid(row=3, column=0, columnspan=2, padx=2, pady=2, sticky=tk.W)

f_entry_var_name = tk.StringVar()
f_entry_var_dob = tk.StringVar()

f_entry_name = ttk.Entry(forget_frame, width=32, textvariable=f_entry_var_name)
f_entry_dob = ttk.Entry(forget_frame, width=32, textvariable=f_entry_var_dob)
f_entry_name.focus()
f_entry_name.grid(row=2, column=3, columnspan=2, padx=2, pady=2)
f_entry_dob.grid(row=3, column=3, columnspan=2, padx=2, pady=2)


def f_clearall():
    f_entry_name.delete(0, tk.END)
    f_entry_dob.delete(0, tk.END)
    f_entry_name.focus()


def f_submit():
    f_user_name = f_entry_var_name.get().title()
    f_user_dob = f_entry_var_dob.get()
    with open('Login_data.csv', 'r') as f:
        csv_reader = DictReader(f)
        for row in csv_reader:
            if f_user_name == (row['First_Name'] + ' ' + row['Last_Name']) and f_user_dob == row['DOB']:
                msg = 'Your Username is "' + row['Username'] + '" and Password is "' + row['Password'] + '".'
                m_box.showinfo('Password', msg)
                f_clearall()
                break
        else:
            m_box.showerror('Error', 'Your details does not match')


f_btn_submit = ttk.Button(forget_frame, text='Get Password', command=f_submit)
f_btn_clear = ttk.Button(forget_frame, text='Clear', command=f_clearall)
f_btn_login = ttk.Button(forget_frame, text='Go to Login Page', command=login)
f_btn_submit.grid(row=5, column=0)
f_btn_clear.grid(row=5, column=2)
f_btn_login.grid(row=5, column=4)

win.mainloop()
