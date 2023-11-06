from tkinter import *
from tkinter import messagebox
# import random
from random import randint,shuffle,choice
import pyperclip
import json

BGCOLOR = '#FFFFFF'

# _____WINDOW____
window = Tk()
window.title('Password manager')
window.minsize(width=350, height=350)
window.config(padx=50, pady=50, bg=BGCOLOR)
# _____Canvac____
canvas = Canvas(width=200, height=200, bg=BGCOLOR, highlightthickness=0)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(110, 100, image=lock_img)
canvas.grid(column=2, row=1)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = randint(8, 10)
nr_symbols = randint(2, 4)
nr_numbers = randint(2, 4)

password_list = []

password_letter = [choice(letters) for _ in range(nr_letters)]
password_symbols = [choice(symbols) for _ in range(nr_symbols)]
password_number = [choice(numbers) for _ in range(nr_numbers)]

# for char in range(nr_letters):
#   password_list.append(random.choice(letters))
#
# for char in range(nr_symbols):
#   password_list += random.choice(symbols)
#
# for char in range(nr_numbers):
#   password_list += random.choice(numbers)
password_list = password_letter + password_symbols + password_number
shuffle(password_list)

password = "".join(password_list)

print(f"Your password is: {password}")


def generete_pass():
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def saved_password():
    website = entry.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email":email,
            "password":password,
        }
    }
    if len(website) == 0:
        messagebox.showinfo("Warrning", "Empty")
        entry.delete(0, END)
        entry_password.delete(0, END)
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the deitails entered : \n Email : {email}"
                                                              f"\nPassword:{password} \n Is it ok to save?")
        if is_ok:
            try:
                with open('data.json', mode='r') as data_file:
                    # data_file.write(f"{website}  |  {email}   |    {password} |\n")
                    # Reading data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('data.json', mode='w') as data_file:
                    # data_file.write(f"{website}  |  {email}   |    {password} |\n")
                    # Reading data
                    json.dump(new_data,data_file)
                    entry.delete(0, END)
                    entry_password.delete(0, END)
            else:
                with open('data.json',mode='w') as data_file:
                    # Update data
                    data.update(new_data)
                    # Saving data
                    json.dump(data,data_file,indent = 4)

            finally:
                entry.delete(0, END)
                entry_password.delete(0, END)

def FindPassWord():
    with open('data.json',mode='r') as data_file:
        data = json.load(data_file)
        website = entry.get()


        # need website ih data
        for k,v in data.items():
            if website == k:
                passw=v['password']
                messagebox.askquestion(title = ')',message=f'Website : {website}\n Pass: {passw}')
                print(f'Website : {website}\n Pass: {passw}')
            else:
                messagebox.showinfo(title = '',message = 'Not Found ')


# ---------------------------- UI SETUP ------------------------------- #
label_web = Label()
label_web.config(width=15, text='Website', bg=BGCOLOR, fg="black")
label_web.grid(column=1, row=2)

entry = Entry()
entry.config(width=19, bg=BGCOLOR, fg="black", highlightthickness=1)
entry.grid(column=2, row=2, padx=10, pady=10)
entry.focus()

button_search = Button()
button_search.config(width=10, bg=BGCOLOR, fg="black", highlightthickness=0, text='Search', relief=RIDGE, borderwidth=0, highlightbackground='white',command =FindPassWord)
button_search.grid(column=3, row=2, padx=10, pady=10)
# ------------------

label_email = Label()
label_email.config(width=15, text='Email/Username', bg=BGCOLOR, fg="black")
label_email.grid(column=1, row=4, padx=10, pady=10)

entry_email = Entry()
entry_email.config(width=35, bg=BGCOLOR, fg="black", highlightthickness=1, borderwidth=1)
entry_email.grid(column=2, row=4, columnspan=2, padx=10, pady=10)
entry_email.insert(0, "vyacheFuros@gmail.com")

label_password = Label()
label_password.config(width=15, text='Password', bg=BGCOLOR, fg="black", borderwidth=1)
label_password.grid(column=1, row=6)

entry_password = Entry()
entry_password.config(width=19, bg=BGCOLOR, fg="black", highlightthickness=1, borderwidth=1)
entry_password.grid(column=2, row=6, padx=10, pady=10)

button_generet = Button()
button_generet.config(width=10, bg=BGCOLOR, fg="black", highlightthickness=0, text='GenPassword', relief=RIDGE,
                      borderwidth=0, highlightbackground='white',command=generete_pass)
button_generet.grid(column=3, row=6, padx=10, pady=10)

button_adding = Button()
button_adding.config(width=30, bg=BGCOLOR, fg="black", highlightthickness=0, text='Add', relief=RIDGE,
                     highlightbackground="white", command=saved_password)
button_adding.grid(column=2, row=8, columnspan=2)

mainloop()
