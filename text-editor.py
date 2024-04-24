from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import colorchooser
root = Tk()
root.title("Text Editor <PRX>")
root.geometry("1090x1080")
 
label = ttk.Label(text="Mini-Word")
label.pack(anchor=NW, padx=10, pady=10)
warn = ttk.Label(text= "Font only for static text :)\n\n\n\n\nThis is test SIMPLIEST program")
warn.pack(anchor=NE)
text=Text(root)
text.pack()

def font_changed(font):
    label["font"] = font
 
def select_font():
    root.tk.call("tk", "fontchooser", "configure", "-font", label["font"], "-command", root.register(font_changed))
    root.tk.call("tk", "fontchooser", "show")
         
def saveas():
    global text  
    t = text.get("1.0", "end-1c")
    savelocation=filedialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

def select_color():
    result = colorchooser.askcolor(initialcolor="black")
    label["foreground"] = result[1]
    text["foreground"] = result[1]

def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != '':
        with open(filepath, "r") as file:
            exp =file.read()
            text.delete('1.0', END)
            text.insert('1.0', exp)

color_button = ttk.Button(text="Color", command=select_color)
color_button.pack(anchor=NW, padx=30, pady=20)

font_button = ttk.Button(text="Font", command=select_font)
font_button.pack(anchor='nw', padx=30, pady=20)

open_button = ttk.Button(text="Open", command=open_file)
open_button.pack(anchor='nw', padx=30, pady = 20)

save_btn = ttk.Button(text= 'Save', command= saveas)
save_btn.pack(anchor='nw', padx= 30, pady=70)

root.mainloop()