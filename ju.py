from tkinter import *
root = Tk()
# creating input
e = Entry(root, width=50)
e.pack()
e.insert(0,"enter ur name: ")
#defining what the button does
def click():
    mylabel= Label(root, text = "your name is " + e.get())
    mylabel.pack()

#creating the button
button = Button(root,text="What's ur name",command=click,fg="red")
button.pack()


root.mainloop()