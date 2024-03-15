import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
window = tk.Tk()
window.geometry("800x500")
global c
c = tk.Canvas(window, height=500, width=800, bg='cyan')
global itext
itext = "Nothing Selected"
color = "cyan"
compilecontents = "import tkinter as tk\nwindow = tk.Tk()\nwindow.title('Untitled')\nc = tk.Canvas(window, height=500, width=800, bg='" + color + "')\nc.pack()"
global buttontext
buttontext = "Button"

digits = 123456789

global filecontents
filecontents = "No Metadata"

def CloseApp():
  exit()

def Compile():
  global compilecontents
  compilecontents = "import tkinter as tk\nwindow = tk.Tk()\nwindow.title('Untitled')\nc = tk.Canvas(window, height=500, width=800, bg='" + color + "')\nc.pack()"
  if filecontents == "element=1":
    compilecontents = compilecontents + "\nelement = tk.Button(window, text='" + buttontext +"', font=('arial'))\nelement.place(x=90, y=90)\nwindow.mainloop()"
  else:
    compilecontents = compilecontents + "\nwindow.mainloop()"
  print()
  file = filedialog.asksaveasfile(title = "Game  File", defaultextension=".pyw", filetypes=[("Consoless Python File", "*.pyw")])
  if file:
    file.write(compilecontents)
    file.close()
  messagebox.showinfo(title="Icengine", message="Game Built")

def tbd():
  return

def Open():

  global tf
  global c
  global element
  tf = filedialog.askopenfilename(
        initialdir="Desktop", 
        title="Open Color Metadata", 
        filetypes=(("Icengine Project Metadata", "*.ice"),("All Files", "*.*"))
        )
  tf = open(tf, "r")
  global data
  data = tf.read()
  global filedata
  filedata = tf.readline()
  if not data == "":
    c.pack_forget()
    c = tk.Canvas(window, height=500, width=800, bg=data)
    main()

  tf = filedialog.askopenfilename(
        initialdir="Desktop", 
        title="Open Existant Metadata", 
        filetypes=(("Icengine Project Metadata", "*.ice"),("All Files", "*.*"))
        )
  tf = open(tf, "r")
  data = tf.read()
  filedata = tf.readline()
  if data == "element=1":
    element = tk.Button(window, text="Button", font=('arial'), command=showinspector)
  elif data == "No Metadata":
    DeleteButton()
  
  tf = filedialog.askopenfilename(
        initialdir="Desktop", 
        title="Open XPOS Metadata", 
        filetypes=(("Icengine Project Metadata", "*.ice"),("All Files", "*.*"))
        )
  global xpos
  tf = open(tf, "r")
  data = tf.read()
  filedata = tf.readline()
  xpos = int(data)

  tf = filedialog.askopenfilename(
        initialdir="Desktop", 
        title="Open YPOS Metadata", 
        filetypes=(("Icengine Project Metadata", "*.ice"),("All Files", "*.*"))
        )
  tf = open(tf, "r")
  data = tf.read()
  filedata = tf.readline()
  element.place(x=xpos, y=int(data))
  
  

  

  


def Save():
  file = filedialog.asksaveasfile(title = "Save Element Existant File", defaultextension=".ice", filetypes=[("Icengine Project Metadata", "*.ice")])
  if file:
    file.write(filecontents)
    file.close()
  file = filedialog.asksaveasfile(title = "Save Color Metadata File", defaultextension=".ice", filetypes=[("Icengine Project Metadata", "*.ice")])
  if file:
    file.write(color)
    file.close()
  file = filedialog.asksaveasfile(title = "Save X Pos Metadata File", defaultextension=".ice", filetypes=[("Icengine Project Metadata", "*.ice")])
  if file:
    file.write(str(x))
    file.close()
  file = filedialog.asksaveasfile(title = "Save Y Pos Metadata File", defaultextension=".ice", filetypes=[("Icengine Project Metadata", "*.ice")])
  if file:
    file.write(str(y))
    file.close()

def printfc():
  print(filecontents)

def showinspector():
  global inspector
  inspector = tk.Tk()
  inspector.title("Inspector")
  inspectorc = tk.Canvas(inspector, height=600, width=300, bg="gray")
  inspectorc.pack()
  ilabel = tk.Label(inspector, text=itext, font=('Arial', 16))
  ilabel.place(x=20, y=0)
  if itext == "Button":
    global name
    name = tk.Entry(inspector, font=('Arial', 16))
    name.place(x=20, y=40)
    namebtn = tk.Button(inspector, text="Set", command=SetButtonName) 
    namebtn.place(x=20, y=80) 

def CreateButton():
    global element
    global itext
    itext = "Button"
    element = tk.Button(window, text=buttontext, font=('arial'), command=showinspector)
    element.place(x=90, y=90)
    global x
    global y
    x = 90
    y = 90
    showinspector()
    global filecontents
    filecontents = "element=1"

def CreateButtonNoInspector():
    global element
    global itext
    itext = "Button"
    element = tk.Button(window, text=buttontext, font=('arial'), command=showinspector)
    element.place(x=90, y=90)
    global x
    global y
    x = 90
    y = 90



def DeleteButton():
  element.place_forget()

def main():
  window.title("Icengine Beta 2024.0.0f1")
  print("Window Opened!")
  window.update()
  global textbar
  textbar = tk.Entry(window, font=('Arial', 16))
  textbarlabel = tk.Label(window, text="Color", font=('Arial', 16))
  textbarbtn = tk.Button(window, text="Set", font=('Arial', 16), command=SetColor)
  global c
  c.pack()
  textbarlabel.place(x=40, y=380)
  textbar.place(x=40, y=420)
  textbarbtn.place(x=310, y=420)
  menubar = tk.Menu(window)
  filemenu = tk.Menu(menubar, tearoff=0)
  filemenu.add_command(label="Save As", command=Save)
  filemenu.add_command(label="Open", command=Open)
  filemenu.add_command(label="Compile", command=Compile)
  filemenu.add_command(label="Exit", command=CloseApp)
  objmenu = tk.Menu(menubar, tearoff=0)
  objmenu.add_command(label="Create Button Element", command=CreateButton)
  objmenu.add_command(label="Show Inspector", command=showinspector)
  devmenu = tk.Menu(menubar, tearoff=0)
  devmenu.add_command(label="Print Color", command=PrintColor)
  menubar.add_cascade(menu=filemenu, label="File")
  menubar.add_cascade(menu=objmenu, label="GameObject")
  window.config(menu=menubar)

def PrintColor():
  print("the color is " + textbar.get())
  print(compilecontents)
  print("color variable is: " + color)
  global filedata
  print(tf)
  print(filedata)

def SetColor():
  global color
  color = textbar.get()
  global compilecontents
  compilecontents = "import tkinter as tk\nwindow = tk.Tk()\nwindow.title('Untitled')\nc = tk.Canvas(window, height=500, width=800, bg='" + color + "')\nc.pack()"
  global c
  c.pack_forget()
  c = tk.Canvas(window, height=500, width=800, bg=textbar.get())
  main()

def SetButtonName():
  global buttontext
  buttontext = name.get()
  global compilecontents
  global element
  element.place_forget()
  CreateButtonNoInspector()

main()
userpath = os.path.dirname(__file__)
iconpath = userpath + '\\Icon.ico'
print(iconpath)
window.iconbitmap(default=iconpath)
window.mainloop()