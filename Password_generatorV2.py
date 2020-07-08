
import tkinter as tk
import random as r




password = []
window = tk.Tk()
window.title("Password Generator")




# ------------------------------------------- Functions --------------------------------------
def listToString(password):

    string = ""
     
    for ele in password:
        string += ele

    return string

def nb_characters():
    global nb_char
    nb_char = int(ent_characters.get())

def lower_cases_only():
    password.clear()
    for i in range(nb_char):
        lower_cases = chr(r.randint(97, 122))
        password.append(lower_cases)
    
    r.shuffle(password)

def upper_cases():
    password.clear()
    for i in range(nb_char):
        upper_cases = chr(r.randint(65, 90))
        lower_cases = chr(r.randint(97, 122))
        password.append(upper_cases)
        password.append(lower_cases)
    
    r.shuffle(password)
    
def lower_cases_numbers():
    password.clear()
    for i in range(nb_char):
        numbers = chr(r.randint(48, 57))
        lower_cases = chr(r.randint(97, 122))
        password.append(numbers)
        password.append(lower_cases)
    
    r.shuffle(password)

def lower_cases_symbols():
    password.clear()
    for i in range(nb_char):
        symbols = chr(r.randint(33, 64))
        lower_cases = chr(r.randint(97, 122))
        password.append(symbols)
        password.append(lower_cases)
    
    r.shuffle(password)

def upper_cases_numbers():
    password.clear()
    for i in range(nb_char):
        upper_cases = chr(r.randint(65, 90))
        lower_cases = chr(r.randint(97, 122))
        numbers = chr(r.randint(48, 57))
        password.append(numbers)
        password.append(upper_cases)
        password.append(lower_cases)
    
    r.shuffle(password)

def upper_cases_symbols():
    password.clear()
    for i in range(nb_char):
        upper_cases = chr(r.randint(65, 90))
        lower_cases = chr(r.randint(97, 122))
        symbols = chr(r.randint(33, 64))
        password.append(symbols)
        password.append(upper_cases)
        password.append(lower_cases)
    
    r.shuffle(password)

def all_characters():
    password.clear()
    for i in range(nb_char):
        upper_cases = chr(r.randint(65, 90))
        lower_cases = chr(r.randint(97, 122))
        symbols = chr(r.randint(33, 64))
        numbers = chr(r.randint(48, 57))
        password.append(symbols)
        password.append(numbers)
        password.append(upper_cases)
        password.append(lower_cases)
    
    r.shuffle(password)

# -------------------------------- Conditions ----------------------------------

def print_result():

    if (l_state.get() == 1) & (n_state.get() == 0) & (s_state.get() == 0):
        upper_cases()
        lbl_result["text"] = str(listToString(password[0:nb_char]))
    
    elif (l_state.get() == 0) & (n_state.get() == 1) & (s_state.get() == 0):
        lower_cases_numbers()
        lbl_result["text"] = str(listToString(password[0:nb_char]))

    elif (l_state.get() == 0) & (n_state.get() == 0) & (s_state.get() == 1):
        lower_cases_symbols()
        lbl_result["text"] = str(listToString(password[0:nb_char]))

    elif (l_state.get() == 1) & (n_state.get() == 1) & (s_state.get() == 0):
        upper_cases_numbers()
        lbl_result["text"] = str(listToString(password[0:nb_char]))

    elif (l_state.get() == 1) & (n_state.get() == 0) & (s_state.get() == 1):
        upper_cases_symbols()
        lbl_result["text"] = str(listToString(password[0:nb_char]))

    elif (l_state.get() == 1) & (n_state.get() == 1) & (s_state.get() == 1):
        all_characters()
        lbl_result["text"] = str(listToString(password[0:nb_char]))

    else:
        lower_cases_only()
        lbl_result["text"] = str(listToString(password[0:nb_char]))

    

# GUI

l_state = tk.IntVar()
n_state = tk.IntVar()
s_state = tk.IntVar()

lbl_welcome = tk.Label(text="Welcome to Password Generator!", fg="black")
lbl_welcome.pack()

lbl_characters = tk.Label(text="Enter de number of characters you want", fg="black")
lbl_characters.pack()

ent_characters = tk.Entry(fg="blue", width=10)
ent_characters.pack()

btn_characters_submit = tk.Button(text="submit", fg="blue", command=nb_characters)
btn_characters_submit.pack()

c1 = tk.Checkbutton(window, text='Upper Cases', variable=l_state, onvalue=1, offvalue=0)
c1.pack()

c2 = tk.Checkbutton(window, text='Numbers', variable=n_state, onvalue=1, offvalue=0)
c2.pack()

c3 = tk.Checkbutton(window, text='Symbols', variable=s_state, onvalue=1, offvalue=0)
c3.pack()

btn_submit = tk.Button(text="submit", fg="blue", command=print_result)
btn_submit.pack()

lbl_result = tk.Label(text="", fg="black")
lbl_result.pack()

window.mainloop()
