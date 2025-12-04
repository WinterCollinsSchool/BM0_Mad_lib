from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("Three Buttons Example")

#Set size of window
root.geometry("300x150")

# Create buttons
red_button = Button(root, text="Red", background='red')
yellow_button = Button(root,text="Yellow",background='yellow')
green_button = Button(root, text="Green", background='green')
#Add a label
label = Label(root, text="This is a stoplight")

text_box = Text(root)

# Place widgets in window (with pack function!)
red_button.pack()
yellow_button.pack()
green_button.pack()
label.pack()
text_box.pack()

# Start the GUI event loop
root.mainloop()