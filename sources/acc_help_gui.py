import tkinter as tk
from tkinter.constants import BOTTOM, COMMAND, HORIZONTAL, NONE, RIGHT, X, Y
import tkinter.font as tkFont
from pathlib import Path
import global_
#
# Help window
#        Reads README.md file (see global_.py module)
#
class HelpW:
    # tkinter:
    # Using coordinats defination on Windows aplication 
    # components (buttons, texts, entries, etc.) defined by X, Y, coordinats in windows geometry 
    # componanents.grid(column,row), master.rowconfigure(row,...), master.columnconfigure(column,...) methods are not applicable
    def __init__(self, master):
        self.master = master
        self.master.resizable(False,False)
        self.master.geometry("800x500")

        gl = global_.vars()
        self.helpfile = gl.helpfile
        self.fontn = gl.fontd.get('fAndale')
        self.fonts = gl.fontd.get('fs14')
        
        self.HW_labels()
        self.HW_text()
        self.fill_text()
        
    def HW_labels(self):
        self.label1 = tk.Label(self.master, text="Account Manager Help")
        self.label1.pack()
        self.label1.place(x=315,y=10)
        
 
    def HW_text(self):

        txtfont = tkFont.Font(family=self.fontn, size=self.fonts)
        vscrol = tk.Scrollbar(self.master)
        hscrol = tk.Scrollbar(self.master, orient=HORIZONTAL)

        self.text1 = tk.Text(self.master, 
            height=27, width=90,
            bd=2,
            wrap=NONE,
            font=txtfont )
        self.text1.pack()

        self.text1.place(x=30,y=30)
        self.text1.config(yscrollcommand=vscrol.set)
        self.text1.config(xscrollcommand=hscrol.set)
     
        vscrol.config(command=self.text1.yview)
        vscrol.pack(side=RIGHT, fill=Y )

        hscrol.config(command=self.text1.xview)
        hscrol.pack(side=BOTTOM, fill=X)

   
    def fill_text(self):
        self.text1.delete(1.0, tk.END)
        text = "------------------------------------" + str(self.helpfile) + "------------------------------------"
        f = Path(self.helpfile)
        if f.is_file():
            textl = f.read_text().splitlines()
            for txt in textl:
                if txt == "```sh": txt="\b"
                if txt == "```": txt="\b"
                txt = txt.replace("|","\t")
                txt = txt.replace("**/","/")
                txt = txt.replace("**","")
                text+="\n"+txt
            self.text1.insert(tk.END,text)
        else:
            text+="\n \nHelp file not found"
            self.text1.insert(tk.END,text)
