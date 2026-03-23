from tkinter import *
from PIL import Image , ImageTk
from tkinter import messagebox

window=Tk()
window.geometry("400x400")
window.title("PASSWORD CHECKER")
window.configure(bg="light green")

def check():
    length=len(entry.get())
    if length>5:
        label2=Label(window , text="Perfect Password" , bg="blue" , fg="white")
        label2.pack()
    elif length==5:
        label3=Label(window , text="TRY AGAIN" , bg="pink" , fg="white")
        label3.pack()
    elif length<5:
        label4=Label(window , text="NOT STRONG" , bg="yellow" , fg="white")
        label4.pack()
    else:
        label5=Label(window , text="ERROR" , bg="blue" , fg="white")
        label5.pack()
        messagebox.showerror("ERROR")




label=Label(window , text="Write your password in the entry and then click the CHECK button!" , bg="light blue" , fg="purple")
label.pack()
entry=Entry(window)
entry.pack()
btn=Button(window , text="CHECK" , bg="red" , fg="white" , command=check)
btn.pack()
upload=Image.open("1.jpg")
image=ImageTk.PhotoImage(upload)



window.mainloop()