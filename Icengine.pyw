import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import colorchooser
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
buttontext = "Text"
global projectname
projectname = 'Untitled'
buttoncolor = [
  "None",
  'white'
]
filelist = [
  "element=0\n",
  "white"
]

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
    global btncolor
    name = tk.Entry(inspector, font=('Arial', 16))
    name.place(x=20, y=40)
    name.insert(0, "Text")
    namebtn = tk.Button(inspector, text="Set Name", command=SetButtonName)
    btncolor = tk.Button(inspector, text="Set Color", command=SetButtonColor)
    btncolor.place(x=20, y=120) 
    namebtn.place(x=20, y=80)
    delbtn = tk.Button(inspector, text="Delete", bg="red", command=DeleteButton) 
    delbtn.place(x=20, y=380)

global crashhandler
crashhandler = True

digits = 123456789

global filecontents
filecontents = "element=0"

global element
element = None

def CloseApp():
  exit()

def Compile():
  global compilecontents
  compilecontents = "import tkinter as tk\nwindow = tk.Tk()\nwindow.title('" + projectname + " - Made In Icengine" + "')\nc = tk.Canvas(window, height=500, width=800, bg='" + color + "')\nc.pack()"
  if filecontents == "element=1":
    compilecontents = compilecontents + "\nelement = tk.Button(window, text='" + buttontext +"', bg=('" + buttoncolor + "'), font=('arial'))\nelement.place(x=90, y=90)\nwindow.mainloop()"
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
  global projectname
  global filelist
  global buttoncolor
  global itext
  tf = filedialog.askopenfilename(
        initialdir="Desktop", 
        title="Open Color Metadata", 
        filetypes=(("Icengine Project Metadata", "*.ice"),("All Files", "*.*"))
        )
  tf = open(tf, "r")
  global data
  data = tf.read()
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
  filelist = list(tf.readlines())
  print(filelist[0])
  data = tf.read()
  buttoncolor = filelist[1]
  print(buttoncolor[1])
  print(data)
  try:
    if filelist[0] == 'element=1\n':
      if not element == None:
        element.place_forget()
      element = tk.Button(window, text=buttontext, font=('arial'), bg=buttoncolor[1], command=showinspector)
  except:
    if crashhandler == True:
      messagebox.showerror(title="Icengine Crash Handler", message="Icengine Ran Into An Error And Crashed\nError Code: 001x0002")
      window.destroy()
      playersettings.destroy()
    elif crashhandler == False:
      messagebox.showwarning(title="Crash Handler Failure", message="Icengine Ran Into A Fatal Error But Could Not Crash Due To Disabled Crash Handler, Icengine May No Longer Work\nFailed Error Code: 001x0002")

  else:
    DeleteButton()
  tf = filedialog.askopenfilename(
        initialdir="Desktop", 
        title="Open XPOS Metadata", 
        filetypes=(("Icengine Project Metadata", "*.ice"),("All Files", "*.*"))
        )
  global xpos
  tf = open(tf, "r")
  data = tf.read()
  xpos = int(data)

  tf = filedialog.askopenfilename(
        initialdir="Desktop", 
        title="Open YPOS Metadata", 
        filetypes=(("Icengine Project Metadata", "*.ice"),("All Files", "*.*"))
        )
  tf = open(tf, "r")
  data = tf.read()
  element.place(x=xpos, y=int(data))
  itext = "Button"

  tf = filedialog.askopenfilename(
        initialdir="Desktop", 
        title="Open Project Settings Metadata", 
        filetypes=(("Icengine Project Settings Metadata", "*.icem"),("All Files", "*.*"))
        )
  tf = open(tf, "r")
  data = tf.read()
  projectname = data
  window.title("Icengine Beta 2024.0.0f1 - " + projectname)
  
  

  

  


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
  file = filedialog.asksaveasfile(title = "Save Project Metadata", defaultextension=".icem", filetypes=[("Icengine Project Settings Metadata", "*.icem")])
  if file:
    file.write(projectname)
    file.close

def printfc():
  print(filecontents)

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
    filecontents = "element=1\ncolor='" + str(buttoncolor) + "'\n"

def CreateButtonNoInspector():
    global element
    global itext
    itext = "Button"
    element = tk.Button(window, text=buttontext[1], font=('arial'), bg=buttoncolor, command=showinspector)
    element.place(x=90, y=90)
    global x
    global y
    x = 90
    y = 90

def showplayersettings():
  global projectnamebox
  global playersettings
  playersettings = tk.Tk()
  playersettings.title("Player Settings")
  playersettings.geometry("800x500")
  c = tk.Canvas(playersettings, height=500, width=800, bg='grey')
  c.pack()
  projectnameboxlabel = tk.Label(playersettings, text="Project Name", font=("Arial", 8))
  projectnameboxlabel.place(x=20, y=20)
  projectnamebox = tk.Entry(playersettings)
  projectnamebox.place(x=20, y=40)
  projectnamebtn = tk.Button(playersettings, text="Set", font=("Arial", 8), command=SetProjectName)
  projectnamebtn.place(x=20, y=60)

def DeleteButton():
  global playersettings
  element.place_forget()
  global itext
  itext = "Nothing Selected"
  inspector.destroy()
  global buttontext
  buttontext = "Button"
  global filecontents
  filecontents = "element=0"
  if element.winfo_exists() == 1:
    if filecontents == "element=0":
      if crashhandler == True:
        messagebox.showerror(title="Icengine Crash Handler", message="Icengine Ran Into An Error And Crashed\nError Code: 001x0001")
        window.destroy()
        playersettings.destroy()
      elif crashhandler == False:
        messagebox.showwarning(title="Crash Handler Failure", message="Icengine Ran Into A Fatal Error But Could Not Crash Due To Disabled Crash Handler, Icengine May No Longer Work\nFailed Error Code: 001x0001")

def main():
  global menubar
  global devmenu
  global element
  global filelist
  window.title("Icengine Beta 2024.0.0f1 - " + projectname)
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
  if filelist[1] == "element=1\n":
    CreateButtonNoInspector()
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
  devmenu.add_command(label="Print Log Data", command=PrintColor)
  devmenu.add_command(label="Disable Crash Handler", command=DisableCrash)
  editmenu = tk.Menu(menubar, tearoff=0)
  editmenu.add_command(label="Project Settings", command=showplayersettings)
  menubar.add_cascade(menu=filemenu, label="File")
  menubar.add_cascade(menu=editmenu, label="Edit")
  menubar.add_cascade(menu=objmenu, label="GameObject")
  menubar.add_command(label="Enter Debug Code", command=EnterCode)
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

def SetButtonColor():
  global element
  global buttoncolor
  global filecontents
  buttoncolor = colorchooser.askcolor()
  element.place_forget()
  filecontents = "element=1\n" + str(buttoncolor)
  print(buttoncolor)
  CreateButtonNoInspector()

def SetProjectName():
  global window
  global projectname
  projectname = projectnamebox.get()
  window.title("Icengine Beta 2024.0.0f1 - " + projectname)

def DisableCrash():
  answer = messagebox.askyesno(title="Confirm", message="Are You Sure You Want To Disable Crash Handler (UNSTABLE)")
  if answer == True:
    print("Disabled Crash Handler")
    global crashhandler
    crashhandler = False

def EnterCode():
  codeanswer = simpledialog.askstring("Enter Code", "Enter Code")
  print(codeanswer)
  if codeanswer == "1984":
    menubar.add_cascade(menu=devmenu, label="Debug")
    menubar.delete("Enter Debug Code")
    return
  if codeanswer == None:
    return

  try:
    int(codeanswer)
  except:
    messagebox.showerror(title="Syntax Error", message="Requires Numbers")
    EnterCode()

  if len(codeanswer) < 4:
    messagebox.showerror(title="Syntax Error", message="Not Enough Characters")
    EnterCode()
  
  if len(codeanswer) > 4:
    messagebox.showerror(title="Syntax Error", message="Too Many Characters")
    EnterCode()

  if not codeanswer == "1984":
    if not codeanswer == None:
      if not codeanswer == "1984":
        messagebox.showerror(title="Syntax Error", message="Wrong Code")
        EnterCode()

main()
userpath = os.path.dirname(__file__)
iconpath = userpath + '\\Icon.ico'
print(iconpath)
window.iconbitmap(default=iconpath)
window.mainloop()