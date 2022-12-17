from tkinter import *
from tkinter import ttk
import csv
import heapq as pq


class Main:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('300x300')
        self.window.title('')

        self.LgFrame = Frame(self.window)
        self.LgFrame.pack(fill=BOTH)

        mLabel = Label(self.LgFrame, text='\nSELAMAT DATANG \nDI LAYANAN PENGIRIMAN PAKET\n', font=('Arial', 13, 'bold'))
        mLabel.pack(side=TOP)

        #######################################################
        Fr1 = Frame(self.LgFrame)
        Fr1.pack(fill=X, pady=5)

        lbl1 = Label(Fr1, width=10, text='Username', font=('Helvetica', 12, 'bold'))
        lbl1.pack(side=LEFT, pady=7)

        self.uid = Entry(Fr1, font=('calibri', 12))
        self.uid.pack(side=LEFT, fill=X, pady=9)

        #######################################################
        Fr2 = Frame(self.LgFrame)
        Fr2.pack(fill=X, pady=5)

        lbl2 = Label(Fr2, width=10, text='Password', font=('Helvetica', 12, 'bold'))
        lbl2.pack(side=LEFT, pady=7)

        self.pwd = Entry(Fr2, font=('calibri', 12))
        self.pwd.pack(side=LEFT, fill=X, pady=9)

        #######################################################
        Fr3 = Frame(self.LgFrame)
        Fr3.pack(fill=X, pady=5)

        btL = Button(Fr3, text='Login', command=self.Login)
        btL.pack(side=BOTTOM, pady=7)

        self.window.mainloop()

    def Login(self):
        self.login = []
        with open('login.csv') as file:
            fl = csv.reader(file)
            for i in fl:
                self.login.append(i)
        
        self.menu() if [str(self.uid.get()), str(self.pwd.get())] in self.login else self.not_log()

    def Add(self):
        print(True)
        self.data.append([self.jrk])
        value = []
        with open ('dbpaket.csv', 'w') as file:
            fl = csv.writer(file)
            fl.writerows(self.data)

        print(self.L1.value)
        print(self.L2.value)
        print(self.L3.value)
        print(self.L4.value)

    def not_log(self):
        Fr4 = Frame(self.LgFrame)
        Fr4.pack(fill=X, pady=5)
    
        lbl3 = Label(Fr4, width=10, text='Username atau Password salah!', fg='red')
        lbl3.pack(side=BOTTOM, pady=7, fill=BOTH)

    def menu(self):
        self.data = []
        with open('dbpaket.csv') as file:
            fl = csv.reader(file)
            for i in fl:
                self.data.append(i)

        self.LgFrame.destroy()
        self.window.geometry('900x500')

        ##############################################
        mFrame = Frame(self.window)
        mFrame.pack(fill=BOTH)

        mFr1 = Frame(mFrame)
        mFr1.pack(fill=X, pady=5)

        mLbl1 = Label(mFr1, width=10, text='MENU', font=('Arial',12, 'bold'))
        mLbl1.pack(side=TOP, pady=7, fill=BOTH)

        ##############################################
        mFr2 = Frame(mFrame)
        mFr2.pack(fill=BOTH, pady=5)

        col = ('tanggal', 'pengirim', 'penerima', 'jarak')

        self.tbl = ttk.Treeview(mFr2,columns=col)
        self.tbl.pack()

        self.tbl.heading('#0', text='Barang')
        self.tbl.heading('tanggal', text='Tanggal')
        self.tbl.heading('pengirim', text='Pengirim')
        self.tbl.heading('penerima', text='Penerima')
        self.tbl.heading('jarak', text='Jarak')

        ##############################################
        f = open("dbpaket.csv", "r")

        for index, line in enumerate(f):
            temp = line.rstrip().split(',')
            self.tbl.insert('', END, iid = index, text = temp[0], values = temp[1:])

        #######################################
        mFr8 = Frame(mFrame)
        mFr8.pack(fill=X, pady=5)

        btI = Button(mFr8, text='Insert', command=self.Insert)
        btI.pack()

    def Insert(self):
        ins = Tk()
        ins.title('')
        #######################################
        iFr1 = Frame(ins)
        iFr1.pack(fill=X, pady=5)

        ilbl2 = Label(iFr1, text='Barang\t\t')
        ilbl2.pack(side=LEFT)

        self.bar = Entry(iFr1)
        self.bar.pack(side=LEFT)

        #######################################
        iFr2 = Frame(ins)
        iFr2.pack(fill=X, pady=5)

        ilbl3 = Label(iFr2, text='Tanggal\t\t')
        ilbl3.pack(side=LEFT)

        self.tgl = Entry(iFr2)
        self.tgl.pack(side=LEFT)

        #######################################
        iFr3 = Frame(ins)
        iFr3.pack(fill=X, pady=5)

        ilbl4 = Label(iFr3, text='Pengirim\t')
        ilbl4.pack(side=LEFT)

        self.krm = Entry(iFr3)
        self.krm.pack(side=LEFT)

        #######################################
        iFr4 = Frame(ins)
        iFr4.pack(fill=X, pady=5)

        ilbl5 = Label(iFr4, text='Penerima\t')
        ilbl5.pack(side=LEFT)

        self.trm = Entry(iFr4)
        self.trm.pack(side=LEFT)
        
        #######################################
        iFr5 = Frame(ins)
        iFr5.pack(fill=X, pady=5)

        Label(iFr5, text='Jarak\t\t').pack(side=LEFT)

        self.jrk = Entry(iFr5)
        self.jrk.pack(side=LEFT)

        ######################################
        iFr6 = Frame(ins)
        iFr6.pack(fill=X, pady=5)

        Label(iFr6, text='Layanan Yang Dipilih:').pack()
        # self.L1 = Radiobutton(iFr6, indicatoron=0, text='Layanan YES',value=3  ).pack() 
        # self.L2 = Radiobutton(iFr6, indicatoron=0, text='Layanan  SS',value=2 ).pack()
        # self.L3 = Radiobutton(iFr6, indicatoron=0, text='Layanan REG',value=1 ).pack()
        # self.L4 = Radiobutton(iFr6, indicatoron=0, text='Layanan OKE',value=0.5).pack()
        entry = Entry(text = 'Pelayanan', font = ('calibre',10,'bold'))

        #######################################
        iFr7 = Frame(ins)
        iFr7.pack(fill=X, pady=5)

        iBtn = Button(iFr7, text='Insert', command=self.Add)
        iBtn.pack()
        
        ins.mainloop()

if __name__ == '__main__':
    Main()