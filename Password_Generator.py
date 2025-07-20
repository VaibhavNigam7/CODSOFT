from tkinter import *
import random
import string

window = Tk()
window.title("Password Generator")
window.geometry('400x200')


label = Label(window, text="Length of the password:", font=("Arial", 15))
label.place(x=10, y=20)

entry = Entry(window)
entry.place(x=200, y=20)

result_label = Label(window, text="", font=("Arial", 15))
result_label.place(x=10, y=100)

def pass_generate():
    try:
        length = int(entry.get())
        if length <= 4:
            result_label.config(text="Password too short (min 5 chars)")
        else:
            characters = string.ascii_letters + string.digits + string.punctuation
            random_string = ''.join(random.choices(characters, k=length))
            result_label.config(text="Password: " + random_string)
    except ValueError:
        result_label.config(text="Please enter a valid number")


b = Button(window, text="Generate Password", command=pass_generate)
b.place(y=60, x=130)

window.mainloop()