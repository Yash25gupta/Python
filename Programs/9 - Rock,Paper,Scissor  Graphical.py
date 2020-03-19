import random
import tkinter as tk
from tkinter import ttk
user_score = comp_score = 0

win = tk.Tk()
win.title('Rock-Paper-Scissor')
win.geometry('500x250')

def action(btn):
    global user_score, comp_score
    user_pick = btn.cget('text')
    label2.configure(text='User Choise : ' + user_pick)
    comp_pick = random.choice(('Rock', 'Paper', 'Scissor'))
    label3.configure(text='Computer Choose : ' + comp_pick)
    if comp_pick == user_pick:
        label4.configure(text='Same Choice')
    elif (comp_pick=='Paper' and user_pick=='Scissor') or (comp_pick=='Scissor' and user_pick=='Rock') or (comp_pick=='Rock' and user_pick=='Paper'):
        user_score += 1
        label4.configure(text='You win !!!')
    else:
        comp_score += 1
        label4.configure(text='Computer win !!!')
    label5.configure(text='Your Score : ' + str(user_score))
    label6.configure(text='Computer Score : ' + str(comp_score))

game_frame = ttk.LabelFrame(win)
game_frame.grid(row=0, column=0, rowspan=4, padx=20, pady=20)

label1 = tk.Label(game_frame, text='Choose any from Below', font=('Helvetica',12,'bold'))
label1.grid(row=0, column=0, pady=1)

label2 = tk.Label(win, text='User Choise : ', font=('Helvetica',12,'bold'))
label3 = tk.Label(win, text='Computer Choose : ', font=('Helvetica',12,'bold'))
label4 = tk.Label(win, text='', font=('Helvetica',16,'bold'))
label5 = tk.Label(win, text='Your Score : ', font=('Helvetica',11,'bold'))
label6 = tk.Label(win, text='Computer Score : ', font=('Helvetica',11,'bold'))

label2.grid(row=0, column=2, pady=1)
label3.grid(row=1, column=2, pady=1)
label4.grid(row=2, column=2, pady=1)
label5.grid(row=3, column=2, pady=1)
label6.grid(row=4, column=2, pady=1)

btn1 = ttk.Button(game_frame, text='Rock', command=lambda: action(btn1))
btn2 = ttk.Button(game_frame, text='Paper', command=lambda: action(btn2))
btn3 = ttk.Button(game_frame, text='Scissor', command=lambda: action(btn3))

btn1.grid(row=2, column=0, sticky=tk.W, padx=50, pady=10)
btn2.grid(row=3, column=0, sticky=tk.W, padx=50, pady=10)
btn3.grid(row=4, column=0, sticky=tk.W, padx=50, pady=10)

win.mainloop()

