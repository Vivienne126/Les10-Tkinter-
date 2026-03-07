from tkinter import*
window=Tk()
window.title("Sample Window")
window.geometry("300x300")

label1=Label(text="Hello User" , fg="Black" , bg="White")
btn1=Button(text="Click me" , fg="white" , bg="Black")
entry=Entry(fg="yellow" , bg="blue" , width=50)
label1.pack()
btn1.pack()
entry.pack()

frame=Frame(master=window , relief=RAISED , borderwidth=5)
frame.pack()
label2=Label(master=frame , text="Sample Frame" )
label2.pack()

textbox=Text(fg="green" , bg="yellow")
textbox.pack()

window.mainloop()
