from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from tkinter import colorchooser
window=Tk()
def open_file():
    path=filedialog.askopenfilename()
    print(path)
    f=open(path,"r")
    inp=str(f.read())
    print(inp)
    tri=f.read()
    text.insert(tk.END,inp)
    f.close()
def save_file():
    fil=filedialog.asksaveasfile(defaultextension=".txt",filetypes=[("text file",".txt"),
                                                                    ("pdf file",".pdf"),
                                                                    ("html file",".html"),
                                                                    ("JPEG graphic",".JPG")])
    data=text.get("1.0",END)
    fil.write(data)
    fil.close()
def exitonce():
           ans=messagebox.askyesnocancel(title="CHECK",message="Do you want to save your file")
           if ans==True:
                 save_file()
           elif ans==FALSE:
                 quit()
           print()
def cleartext():
    if messagebox.askyesno(title="CHECK",message="Do you want to clear text area without saving"):
          text.delete('1.0', END)
def bold():
      text.config(font=('bold',10,'bold'))
      print("BOLD")
def italic():
      text.config(font=('italic',10,'bold'))
      print("italic")
def bold_italic():
      text.config(font=('bold italic',10,'bold'))
      print("Bold italic")
def sizeof():
      open=Tk()
      open.title("Choose the size of text")
      scale=Scale(open,
            font=('bold',20),
            orient=HORIZONTAL,
            fg="red",
            bg="black",
            activebackground="green",
            tickinterval=5,
            length=1000
            )
      text.config(font=('bold',int(scale.get()),'bold'))
      print(int(scale.get()))
      scale.set(50)
      scale.pack()
def col():
      print()
      color=colorchooser.askcolor()
      print(color)
      text.config(background=color[1])
def colu():
      print()
      color=colorchooser.askcolor()
      print(color)
      text.config(foreground=color[1])
window.title("NOTE-PAD")
icon=PhotoImage(file="notpad.png")
save=PhotoImage(file="save.png")
window.iconphoto(True,icon)
window.geometry("400x400")
men=Menu(window)
window.config(menu=men)
filemenu=Menu(men,tearoff=0)
editmenu=Menu(men,tearoff=0)
font=Menu(men,tearoff=0)
men.add_cascade(label="File",menu=filemenu)
men.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="clear",command=cleartext)
editmenu.add_command(label="Size",command=sizeof)
editmenu.add_command(label="Back Ground color",command=col)
editmenu.add_command(label="Foreground Ground color",command=colu)
editmenu.add_cascade(label="font",menu=font)
font.add_command(label="Bold",command=bold)
font.add_command(label="Arial",command=italic)
font.add_command(label="Bold Italic",command=bold_italic)
filemenu.add_command(label="OPEN",command=open_file)
filemenu.add_command(label="SAVE",command=save_file)
filemenu.add_separator()
filemenu.add_command(label="EXIT",command=exitonce)
text=Text(window,bg="light yellow")
text.config(width=400,height=400)
text.pack()
window.mainloop()