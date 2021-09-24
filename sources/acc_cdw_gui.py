import tkinter as tk
import tkinter.font as tkFont
import traceback
import tkinter.messagebox
import getdbv
import chgdeluser
#
# Data Entry window
#        for new account insertion.
#
class ChangeDeleteW:
    # tkinter:
    # Using coordinats defination on Windows aplication 
    # components (buttons, texts, entries, etc.) defined by X, Y, coordinats in windows geometry 
    # componanents.grid(column,row), master.rowconfigure(row,...), master.columnconfigure(column,...) methods are not applicable
    def __init__(self, master, id):
        self.master = master
        self.master.resizable(False,False)
        self.master.geometry("600x400")
        
        self.id = id
        
        row = chgdeluser.get_user(self.id)
        
        self.actname = self.usrname = self.urlname = self.mailname = self.expln = self.psswrd = tk.StringVar()
        
        global options
        global cnt
        options = ["Standart","e-mail","URL","Bank","System"]
        try:
            cnt = int(row[2])
            self.type = tk.IntVar()
            self.actname = str(row[1])
            self.type = int(row[2]) - 1
            self.usrname = str(row[3])
            self.urlname = str(row[4])
            self.mailname = str(row[5])
            self.expln = str(row[6])
            self.psswrd = str(row[7])
            self.EW_labels()
            self.EW_entries()
            self.EW_options()
            self.EW_buttons()
        except:
            message = 'No Records Found'
            tk.messagebox.showerror('Error',message)
            self.master.destroy()

    def EW_labels(self):
        self.label1 = tk.Label(self.master, text="Account Name:")
        self.label1.pack()
        self.label1.place(x=50,y=50)
        self.label2 = tk.Label(self.master, text="Account Type:")
        self.label2.pack()
        self.label2.place(x=50,y=80)
        self.label2a = tk.Label(self.master, text=":")
        self.label2a.pack()
        self.label2a.place(x=300,y=80)
        self.label3 = tk.Label(self.master, text="Account User:")
        self.label3.pack()
        self.label3.place(x=50,y=110)
        self.label4 = tk.Label(self.master, text="Account URL:")
        self.label4.pack()
        self.label4.place(x=50,y=140)
        self.label5 = tk.Label(self.master, text="Account eMail:")
        self.label5.pack()
        self.label5.place(x=50,y=170)
        self.label6 = tk.Label(self.master, text="Account Exp:")
        self.label6.pack()
        self.label6.place(x=50,y=200)
        self.label7 = tk.Label(self.master, text="Account Pass:")
        self.label7.pack()
        self.label7.place(x=50,y=230)
        self.label8 = tk.Label(self.master, text="> ")
        self.label8['text'] = self.id
        self.label8.pack()
        self.label8.place(x=50,y=380)
        
    def EW_entries(self):
        self.entry1 = tk.Entry(self.master, width=25)
        self.entry1.pack()
        self.entry1.insert(1,self.actname)
        self.entry1.place(x=150,y=50)
        self.entry3 = tk.Entry(self.master, width=25)
        self.entry3.pack()
        if self.usrname != "None" : self.entry3.insert(1,self.usrname)
        self.entry3.place(x=150,y=110)
        self.entry4 = tk.Entry(self.master, width=25)
        self.entry4.pack()
        if self.urlname != "None" : self.entry4.insert(1,self.urlname)
        self.entry4.place(x=150,y=140)
        self.entry5 = tk.Entry(self.master, width=25)
        self.entry5.pack()
        if self.mailname != "None" : self.entry5.insert(1,self.mailname)
        self.entry5.place(x=150,y=170)
        self.entry6 = tk.Entry(self.master, width=25)
        self.entry6.pack()
        if self.expln != "None" : self.entry6.insert(1,self.expln)
        self.entry6.place(x=150,y=200)
        self.entry7 = tk.Entry(self.master, width=25)
        self.entry7.pack()
        self.entry7.insert(1,self.psswrd)
        self.entry7.place(x=150,y=230)
        
    def EW_options(self):
        self.varss = tk.StringVar(self.master)
        global options
        
        self.varss.set(options[self.type])
        self.optmenu1 = tk.OptionMenu(self.master, self.varss, *options, command=self.option_changed)
        self.optmenu1.pack()
        self.optmenu1.place(x=150,y=80)
        
    def EW_buttons(self):
        self.quitButton = tk.Button(self.master, text = 'Quit', width = 10, command = self.close_windows)
        self.quitButton.pack()
        self.quitButton.place(x=50, y=350)
        self.enterButton = tk.Button(self.master, text = 'Enter', width = 10, command = self.update_data)
        self.enterButton.pack()
        self.enterButton.place(x=150, y=350)
        
 
        
    def option_changed(self, *args):
        global cnt
        global options
        # Get index of selected options
        for count, item in  enumerate(options):
            if item==self.varss.get():
                cnt = count + 1
                break
        
    def update_data(self):
        global cnt
        acnc = actc = usrc = pasc = urlc = emlc =  expc = False
        actname=acttype=usrname=urlname=emlname=explain=passwrd = None
        try:
            #self.label2a['text'] = str(cnt)
            acttype = cnt
            actc = True
            # Account name entry control
            if self.entry1.get():
                actname = str(self.entry1.get())
                if self.entry_control(actname):
                    acnc = True
                else:
                    message = 'Unsupported letter using'
                    tk.messagebox.showerror('Error',message)
                    self.entry1.focus_set()
            # Account user entry control
            if self.entry3.get():
                usrname = str(self.entry3.get())
                if self.entry_control(usrname):
                    usrc = True
                else:
                    message = 'Unsupported letter using'
                    tk.messagebox.showerror('Error',message)
                    self.entry3.focus_set()
            # Account URL entry control
            if self.entry4.get():
                urlname = str(self.entry4.get())
                if self.entry_control(urlname):
                    urlc = True
                else:
                    message = 'Unsupported letter using'
                    tk.messagebox.showerror('Error',message)
                    self.entry4.focus_set()
            # Account e-mail entry control
            if self.entry5.get():
                emlname = str(self.entry5.get())
                if self.entry_control(emlname):
                    emlc = True
                else:
                    message = 'Unsupported letter using'
                    tk.messagebox.showerror('Error',message)
                    self.entry5.focus_set()
            # Account explain entry control
            if self.entry6.get():
                explain = str(self.entry6.get())
                if self.entry_control(explain):
                    expc = True
                else:
                    message = 'Unsupported letter using'
                    tk.messagebox.showerror('Error',message)
                    self.entry6.focus_set()
            # Password entry control
            if self.entry7.get():
                passwrd = str(self.entry7.get())
                if self.entry_control(passwrd):
                    pasc = True
                else:
                    message = 'Unsupported letter using'
                    tk.messagebox.showerror('Error',message)
                    self.entry7.focus_set()
            if acnc: 
                if actc:
                     if pasc:
                        if (usrc or urlc or emlc):
                            actid = self.id
                            msg = "> "
                            msg = chgdeluser.update_user(actid,actname,acttype,usrname,urlname,emlname,explain,passwrd)
                            self.label8['text'] = msg
                            self.entry1.delete(0, tk.END)
                            self.entry3.delete(0, tk.END)
                            self.entry4.delete(0, tk.END)
                            self.entry5.delete(0, tk.END)
                            self.entry6.delete(0, tk.END)
                            self.entry7.delete(0, tk.END)
                            self.entry1.focus_set()
                        else:
                                message = 'kullanıcı adı veya web adresi veya e-posta bilgilerinden en az biri girilmelidir.'
                                tk.messagebox.showerror('Error',message)
                                self.entry6.focus_set()
            else:
                self.label8['text'] = "Kayıt yapılmadı."
        except:
            # self.label2a['text'] = "Type Error"
            # message = 'Hesap tipi seçiniz'
            #message = " "
            message = traceback.format_exc()
            tk.messagebox.showerror('Error',message)

    def entry_control(self,entryy):
        letters = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","q","r","s","ş","t","u","ü","v","w","x","y","z",
                   "A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","Q","R","S","Ş","T","U","Ü","V","W","X","Y","Z",
                   "0","1","2","3","4","5","6","7","8","9","-","_","*","?","=","(",")","[","]","/","&","%","+","$","^","#","'","!",">","<","|","@",
                   ".",",",";",":"," "]
        cntt = 0
        # Entry data validation loops 
        lene = len(entryy)
        for i in range(lene):
            for ltr in letters:
                if entryy.find(ltr,i,i+1) > -1:
                    cntt=cntt+1
        #print(str(cntt),":",str(cntf))
        if cntt == lene:
            return True
        else:
            return False

    def close_windows(self):
        self.master.destroy()