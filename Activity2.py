from tkinter import*
window=Tk()

for i in range(5):
    for j in range(5):
        frame=Frame(master=window , relief=RAISED , borderwidth=1)
        frame.grid(row=i , column=j , padx=5 , pady=5)
        label=Label(master=frame , text=f"Row {i} , Column {j}")
        label.pack()

window.mainloop()