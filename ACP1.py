from tkinter import *
import random

window = Tk()

window.geometry("400x200")
window.title("Random password generator")

def generate_password():
    lower_case=list("abcdefghijklmnopqrstuvwxyz")
    upper_case=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers=list("0123456789")
    symbol=["!" ,"@" , "#" , "$" , "%" , "^" , "&" , "*"]

    all_chars = lower_case + upper_case + numbers + symbol

    password=random.sample(all_chars, k=12)

    label2 = Label(window, text=password, fg="red", bg="purple")
    label2.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()

label = Label(master=frame, text="WELCOME TO RANDOM PASSWORD GENERATOR", fg="white", bg="black")
label.pack()

btn = Button(master=frame, text="generate", fg="yellow", bg="green", command=generate_password)
btn.pack()

window.mainloop()