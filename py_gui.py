import tkinter as tk
from tkinter import filedialog, Text
import os
#os help me create the gui and allows to run the apps, filedialog is gonna help us pick the apps

root = tk.Tk()

def addApp():
    filename = filedialog.askopenfilename(initialdir="/", title = "Select File", 
    filetypes = (("executables","*.exe"),("all files", "*.*")))


canvas = tk.Canvas(root, height = 350, width=350, bg="#263D42")
canvas.pack()

openfile = tk.Button(root, text = "Open file", padx=10, pady=5, fg="black",command=addApp)
openfile.pack()

runApps = tk.Button(root, text = "Run apps", padx=10, pady=5, fg="black")
runApps.pack()

root.mainloop()

# modificare
