#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import tkinter as tk
import random as r
#from random import choices

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!''@','%','?','&','*']
letters_numbers = letters + numbers
letters_symbols = letters + symbols
numbers_symbols = numbers + symbols
letters_numbers_symbols = letters + numbers + symbols

letters_state = True
numbers_state = True
symbols_state = True


window = tk.Tk()
window.title("Password Generator")

# Functions
def listToString(password):  
    
    string = ""  
     
    for ele in password:  
        string += ele   
      
    return string 
        
def nb_characters ():
    global nb_char
    nb_char = int(ent_characters.get())
    

def print_result():

    if (l_state.get() == 1) & (n_state.get() == 0) & (s_state.get() == 0) :
        password = r.choices(letters, k = nb_char)
        lbl_result["text"]= str(listToString(password))

    elif (l_state.get() == 0) & (n_state.get() == 1) & (s_state.get() == 0):
        password = r.choices(numbers, k = nb_char)
        lbl_result["text"]= str(listToString(password))

    elif (l_state.get() == 0) & (n_state.get() == 0) & (s_state.get() == 1):
        password = r.choices(symbols, k = nb_char)
        lbl_result["text"]= str(listToString(password))

    elif (l_state.get() == 1) & (n_state.get() == 1) & (s_state.get() == 0):
        password = r.choices(letters_numbers, k = nb_char)
        lbl_result["text"]= str(listToString(password))

    elif (l_state.get() == 1) & (n_state.get() == 0) & (s_state.get() == 1):
        password = r.choices(letters_symbols, k = nb_char)
        lbl_result["text"]= str(listToString(password))

    elif (l_state.get() == 0) & (n_state.get() == 1) & (s_state.get() == 1):
        password = r.choices(numbers_symbols, k = nb_char)
        lbl_result["text"]= str(listToString(password))

    elif (l_state.get() == 1) & (n_state.get() == 1) & (s_state.get() == 1):
        password = r.choices(letters_numbers_symbols, k = nb_char)
        lbl_result["text"]= str(listToString(password))

    else:
        print('Please check a box!')


# GUI

l_state = tk.IntVar()
n_state = tk.IntVar()
s_state = tk.IntVar()

lbl_welcome = tk.Label(text = "Welcome to Password Generator!",fg = "black")
lbl_welcome.pack()

lbl_characters = tk.Label(text = "Enter de number of characters you want",fg = "black")
lbl_characters.pack()

ent_characters = tk.Entry(fg="blue", width = 10)
ent_characters.pack()

btn_characters_submit = tk.Button(text="submit", background = "green", fg = "blue",command = nb_characters)
btn_characters_submit.pack()

c1 = tk.Checkbutton(window, text='Letters',variable=l_state, onvalue=1, offvalue=0)
c1.pack()

c2 = tk.Checkbutton(window, text='Numbers',variable=n_state, onvalue=1, offvalue=0)
c2.pack()

c3 = tk.Checkbutton(window, text='Symbols',variable=s_state, onvalue=1, offvalue=0)
c3.pack()

btn_submit = tk.Button(text="submit", background = "green", fg = "blue",command = print_result)
btn_submit.pack()

lbl_result = tk.Label(text = "",fg = "black")
lbl_result.pack()

window.mainloop()