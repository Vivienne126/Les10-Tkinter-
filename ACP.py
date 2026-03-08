from tkinter import*
import random

window=Tk()




def generate_password():
    lower_case=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    upper_case=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numbers=["1","2","3","4","5","6","7","8","9","0"]
    symbol=["!" ,"@" , "#" , "$" , "%" , "^" , "&" , "*" , "()"]

    all=lower_case+upper_case+numbers+symbol
    password=random.sample(all, k=12)
    label2=Label(text=password , fg="red" , bg="purple")

    label2.pack()




frame=Frame(master=window , relief=RAISED , borderwidth=5)
label=Label(master=frame , text="WELCOME TO RANDOM PASSWORD GENERATOR" , fg="white" , bg="black" )
btn=Button(master=frame , text="generate" , fg="yellow" , bg="green" , command=generate_password)
frame.pack()
label.pack()
btn.pack()


window.mainloop()