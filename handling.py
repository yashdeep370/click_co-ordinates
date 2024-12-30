# /handling events

from tkinter import *

def harry(event):
    print(f"you clicked it{event.x},{event.y}")

root = Tk()
root.title("events")

root.geometry("644x334")
widget = Button(root,text="click me")
widget.pack()

widget.bind('<Button-1>',harry)
widget.bind('<Double-1>',quit)


root.mainloop()