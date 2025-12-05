from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("Stop Light")

#Set size of window
root.geometry("300x150")

# Create buttons
red_button = Button(root, text="Red", background='red')
yellow_button = Button(root,text="Yellow",background='yellow')
green_button = Button(root, text="Green", background='green')
light = Button(root, text="Color of LIGHT")
#Add a label
label = Label(root, text="What color is the light?!")

text_box = Text(root,height=15,width=50)

# Place widgets in window (with pack function!)
red_button.grid(row=0,column=0,padx=5)
yellow_button.grid(row=0,column=1,padx=5)
green_button.grid(row=0,column=2,padx=5)
label.grid(row=1,column=1,pady=5)
text_box.grid(row=2,column=1, columnspan=2,padx=5)
light.grid(row=2,column=0,padx=5)

# Start the GUI event loop
root.mainloop()