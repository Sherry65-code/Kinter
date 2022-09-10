try:
    from tkinter import Tk, PhotoImage, Button, Label, font
except Exception as e:
    from os import system,name
    if (name == "nt"):
        print("GUI Error. Check Python Installation.")
    else:
        system("sudo pacman -Sy tk --noconfirm")
        system("sudo apt update && sudo apt install python3-tk --assume-yes")
root = ""
def init():
    global root
    root = Tk()
def basicAuto():
    init()
    setBack("#000000")
    setSize(500, 400)
    setTitle("Its kinter")
    setIcon("sample.png")
    run()
def setResizable(isResizable):
    global root
    if (isResizable):
        root.resizable(0,0)
def setTitle(title):
    global root 
    root.title(f"{title}")
def setSize(width, height):
    global root
    root.geometry(f"{width}x{height}")
def setBack(color):
    global root
    root.config(bg=f"{color}")
def setIcon(iconloc):
    global root, PhotoImage
    root.iconphoto(False, PhotoImage(file=f"{iconloc}"))
def run():
    global root
    root.mainloop()