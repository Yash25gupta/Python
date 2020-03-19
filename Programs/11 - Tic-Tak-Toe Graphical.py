import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box

win = tk.Tk()
win.title('Tic-Tak-Toe')
win.geometry('500x250')

game_frame = ttk.LabelFrame(win)
game_frame.grid(row=0, column=0, rowspan=6, columnspan=6, padx=20, pady=20)

timeclicked = 0

def player():
    global timeclicked
    timeclicked +=1
    if timeclicked % 2 == 0:
        return 'O'
    return 'X'

def player_win():
    if btn1.cget('text') == btn2.cget('text') == btn3.cget('text') != '' : return True
    if btn4.cget('text') == btn5.cget('text') == btn6.cget('text') != '' : return True
    if btn7.cget('text') == btn8.cget('text') == btn9.cget('text') != '' : return True
    if btn1.cget('text') == btn4.cget('text') == btn7.cget('text') != '' : return True
    if btn2.cget('text') == btn5.cget('text') == btn8.cget('text') != '' : return True
    if btn3.cget('text') == btn6.cget('text') == btn9.cget('text') != '' : return True
    if btn1.cget('text') == btn5.cget('text') == btn9.cget('text') != '' : return True
    if btn3.cget('text') == btn5.cget('text') == btn7.cget('text') != '' : return True
    return False

def btn_action(btn):
    per = player()
    if per == 'X':
        btn.configure(text='X', state=tk.DISABLED)
    else:
        btn.configure(text='O', state=tk.DISABLED)
    if player_win():
        if per == 'X':
            s = label3.cget('text') + 1
            label3.configure(text=s)
        if per == 'O':
            s = label4.cget('text') + 1
            label4.configure(text=s)
        m_box.showinfo('Win', 'Player ' + per + ' wins!!!')
        clear()

def clear():
    global timeclicked
    timeclicked = 0
    btns = (btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    for i in btns:
        i.configure(text='', state=tk.NORMAL)

label0 = ttk.Label(win, text='SCORE', font=('Helvetica',18,'bold'))
label1 = ttk.Label(win, text='Player X', font=('Helvetica',14,'bold'))
label2 = ttk.Label(win, text='Player O', font=('Helvetica',14,'bold'))
label3 = ttk.Label(win, text=0, font=('Helvetica',14,'bold'))
label4 = ttk.Label(win, text=0, font=('Helvetica',14,'bold'))

label0.grid(row=0, column=8, columnspan=3, padx=2, pady=2)
label1.grid(row=1, column=8, padx=2, pady=2, sticky=tk.E)
label2.grid(row=1, column=10, padx=2, pady=2, sticky=tk.W)
label3.grid(row=2, column=8, padx=2, pady=2)
label4.grid(row=2, column=10, padx=2, pady=2)

btn1 = tk.Button(game_frame, text='', command=lambda: btn_action(btn1), cursor='top_left_arrow', width=6, height=3)
btn2 = tk.Button(game_frame, text='', command=lambda: btn_action(btn2), cursor='top_left_arrow', width=6, height=3)
btn3 = tk.Button(game_frame, text='', command=lambda: btn_action(btn3), cursor='top_left_arrow', width=6, height=3)
btn4 = tk.Button(game_frame, text='', command=lambda: btn_action(btn4), cursor='top_left_arrow', width=6, height=3)
btn5 = tk.Button(game_frame, text='', command=lambda: btn_action(btn5), cursor='top_left_arrow', width=6, height=3)
btn6 = tk.Button(game_frame, text='', command=lambda: btn_action(btn6), cursor='top_left_arrow', width=6, height=3)
btn7 = tk.Button(game_frame, text='', command=lambda: btn_action(btn7), cursor='top_left_arrow', width=6, height=3)
btn8 = tk.Button(game_frame, text='', command=lambda: btn_action(btn8), cursor='top_left_arrow', width=6, height=3)
btn9 = tk.Button(game_frame, text='', command=lambda: btn_action(btn9), cursor='top_left_arrow', width=6, height=3)
btn_clear = tk.Button(win, text='Clear', command=clear, width=10, height=2)

btn1.grid(row=0, column=0, padx=4, pady=4)
btn2.grid(row=0, column=1, padx=4, pady=4)
btn3.grid(row=0, column=2, padx=4, pady=4)
btn4.grid(row=1, column=0, padx=4, pady=4)
btn5.grid(row=1, column=1, padx=4, pady=4)
btn6.grid(row=1, column=2, padx=4, pady=4)
btn7.grid(row=2, column=0, padx=4, pady=4)
btn8.grid(row=2, column=1, padx=4, pady=4)
btn9.grid(row=2, column=2, padx=4, pady=4)
btn_clear.grid(row=5, column=9, padx=4, pady=4)

win.mainloop()

