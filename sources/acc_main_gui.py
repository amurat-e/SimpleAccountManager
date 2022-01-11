import tkinter as tk
from tkinter import PhotoImage, ttk
from tkinter.constants import LEFT 
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename, asksaveasfilename
import dbinfo
import getuser
import acc_ew_gui
import acc_cdw_gui
import acc_help_gui
import global_

#
# Main GUI module of Accunt Manager 
# lists accounts informations those given full or partial account name
# provides new account entries and entry changes
#
class MainW:
    # tkinter:
    # Using grid defination on Windows aplication 
    # components (buttons, texts, entries, etc.) defined by rows and columns in windows geometry 
    # componanents.pack() and components.place(x,y) methods are not applicable
    
    def __init__(self, master, **kwargs):
        self.master = master
        self.master.geometry("1050x500")
        self.master.resizable(False,False)
        self.master.title("Account Manager   AME ©")

        self.strowss=list()
        self.helpicon = global_.vars().helpicon
        self.fontn = global_.vars().fontd.get('fCArchivo')
        self.fonts = global_.vars().fontd.get('fs13')
        self.db = dbinfo.getinf()       
        
        self.master.rowconfigure(0, weight=0)
        self.master.rowconfigure(1, weight=0)
        self.master.rowconfigure(2, weight=5)
        self.master.rowconfigure(3, weight=0)
        self.master.rowconfigure(4, weight=0)
        self.master.rowconfigure(5, weight=0)
        self.master.rowconfigure(6, weight=0)
        self.master.rowconfigure(7, weight=0)
        self.master.rowconfigure(8, weight=2)
        self.master.rowconfigure(9, weight=0)
        
        self.master.columnconfigure(0,weight=0)
        self.master.columnconfigure(1,weight=0)
        self.master.columnconfigure(2,weight=4)
        self.master.columnconfigure(3,weight=0)
        # 
        self.MW_labels()
        self.label3['text']=self.db
        self.MW_tree()
        self.MW_buttons()
        self.MW_entry()
    
    def MW_labels(self):
        self.label1 = tk.Label(self.master, text='Account Name',pady=4)
        self.label1.grid(column=1, row=0, sticky='SEW')
        andlmn16b = tkFont.Font(family='Andale Mono', weight="bold", size=16)
        self.label2 = tk.Label(self.master, text='Account List', font=andlmn16b ,pady=1)
        self.label2.grid(column=2, row=0, sticky='S')
        self.label3 = tk.Label(self.master, pady=1)
        self.label3.grid(column=2, row=9, sticky='SW')
        
    def MW_entry(self):
        self.entry1 = tk.Entry(self.master, width=15)
        self.entry1.grid(column=1, row=1, padx=5, sticky='NEW')
        self.entry1.insert(1,"%")
        self.entry1.focus()
    
    def MW_tree(self):
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=(self.fontn, self.fonts)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=(self.fontn, self.fonts,'bold')) # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
        columns = ("#1","#2","#3","#4","#5","#6","#7")
        self.tree = ttk.Treeview(self.master, columns=columns, show='headings',selectmode='browse',style="mystyle.Treeview")
        self.tree.column("#1",anchor=tk.E,width=30)
        self.tree.heading("#1",text="ID")
        self.tree.column("#2",anchor=tk.W,width=150)
        self.tree.heading("#2",text="ACCOUNT NAME")
        self.tree.column("#3",anchor=tk.W,width=100)
        self.tree.heading("#3",text="USER NAME")
        self.tree.column("#4",anchor=tk.W,width=150)
        self.tree.heading("#4",text="URL")
        self.tree.column("#5",anchor=tk.W,width=150)
        self.tree.heading("#5",text="E-MAIL")
        self.tree.column("#6",anchor=tk.W,width=200)
        self.tree.heading("#6",text="NOTE")
        self.tree.column("#7",anchor=tk.W,width=250)
        self.tree.heading("#7",text="PASSWORD")
        # When tree record selected call function
        # self.tree.bind('<ButtonRelease-1>', self.selectItem)

        vertscroll = tk.Scrollbar(self.master,orient="vertical")
        vertscroll.config(command=self.tree.yview)
        horzscroll = tk.Scrollbar(self.master,orient="horizontal")
        horzscroll.config(command=self.tree.xview)
        self.tree.config(yscrollcommand=vertscroll.set)
        self.tree.config(yscrollcommand=horzscroll.set)
        self.tree.grid(column=2, row=1, rowspan = 6, sticky='NSWE')
        vertscroll.grid(column=3, row=1, rowspan = 6, sticky='NSWE')
        horzscroll.grid(column=2,row=7,sticky='NWE')

    def selectItem(self,a):
        # Returns dictionary data from selected tree 
        curItem = self.tree.focus()
        # print(self.tree.item(curItem))
        currow = self.tree.item(curItem)
        # Get data from key which is values
        itemss=currow.get('values')
        self.newWindow = tk.Toplevel(self.master)
        self.app = acc_cdw_gui.ChangeDeleteW(self.newWindow,str(itemss[0]))
    
    def MW_buttons(self):
        self.button1 = tk.Button(self.master, text = 'List', bd=4, pady=8, width = 15, command = self.get_user)
        self.button1.grid(column=1, row=2, sticky='N')
        self.button1 = tk.Button(self.master, text = 'Change', pady=4, width = 15, command = self.change_delete_window)
        self.button1.grid(column=1, row=4, sticky='N')
        self.button2 = tk.Button(self.master, text = 'New Entry', pady=4, width = 15, command = self.entry_window)
        self.button2.grid(column=1, row=6, sticky='N')
        self.button3 = tk.Button(self.master, text = 'Save CSV', pady=4, width = 15, command = self.save_file)
        self.button3.grid(column=1, row=7, sticky='N')
        self.button4 = tk.Button(self.master, text = 'Quit', pady=8, width = 15, command = self.close_windows)
        self.button4.grid(column=1, row=8)
        imageic = PhotoImage(file=self.helpicon)
        self.button5 = tk.Button(text="Help", image=imageic, compound=LEFT, padx=8, command = self.showhelp)
        self.button5.image = imageic
        self.button5.grid(column=2, row=8, sticky='E')

    def showhelp(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = acc_help_gui.HelpW(self.newWindow)

    def get_user(self):
        """Open a file for editing."""
        self.tree.delete(*self.tree.get_children())
        usrnm = self.entry1.get()
        rowss = getuser.get_user(usrnm)
        self.strowss.clear()
        strh = "ID;HESAP ADI;KULLANICI;URL;E-POSTA;ACIKLAMA;SIFRE\n"
        self.strowss.append(strh)
        for row in rowss:
            self.tree.insert("",tk.END,values=row)
            strr = str(row[0])+";"+str(row[1])+";"+str(row[2])+";"+str(row[3])+";"+str(row[4])+";"+str(row[5])+";"+str(row[6])+"\n"
            self.strowss.append(strr)
            
    # New top level child window using for new account entries
    def entry_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = acc_ew_gui.EntryW(self.newWindow)
        
    def change_delete_window(self):
        try:
            # Returns dictionary data from selected tree 
            curItem = self.tree.focus()
            # print(self.tree.item(curItem))
            currow = self.tree.item(curItem)
            # Get data from key which is values
            itemss=currow.get('values')
            itemss_first = str(itemss[0])
            self.newWindow = tk.Toplevel(self.master)
            self.app = acc_cdw_gui.ChangeDeleteW(self.newWindow,itemss_first)
        except:
            message = "select a record."
            tk.messagebox.showerror('Error',message)
        
    def save_file(self):
        # Save the current file as a new file.
        filepath = asksaveasfilename(
            defaultextension="csv",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            for rows in self.strowss:
                output_file.write(rows)
            message = (f"File saved  - {filepath}")
            tk.messagebox.showinfo('Information',message)
    
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = MainW(root)
    root.mainloop()

if __name__ == '__main__':
    main()