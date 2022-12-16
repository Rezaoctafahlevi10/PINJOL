# import csv
# from datetime import datetime
# import os
# import time
# from  functools import reduce
# # a = [1, 2, 3, 4]
# # sum_a = reduce(lambda x, y:x+y, a)
# # print(sum_a)

# #kekurangan :
# #1. data admin ==> database admin, dan nanti admin bisa ngefilter sesuai keinginan dan sum total peminjamna (di menu pilihan dan buat databasenya)


# waktu = datetime.now()
# hari = waktu.day
# bulan = waktu.month
# tahun = waktu.year
# tanggal="{}/{}/{}".format(hari,bulan,tahun)

# #Meriview materi cvs metode read 
# # with open('login.csv','r')as logincsv :
# #     reader = csv.DictReader(logincsv)
# #     for row in reader:
# #         print(row)

# def pinjam (): 
#     fBunga = lambda x,y : x*0,5/y


# def pilihan ():
#     print('NB : Bunga cuma 5% dan sudah termasuk biaya admin\n')
#     print('NO |\tPeminjaman        |')
#     print ('1\t', 500000)
#     choise1 = 500000
#     print('2\t',1000000)
#     choise2=1000000
#     print ('3\t',1500000)
#     choise3=1500000
#     print ('4\t',2000000)
#     choise3=2000000
#     user = (input('masukan pilihan : '))

#     fBunga = lambda x, y : (x+x*0.5)/y
#     if user == '1' :
#             print('3 angsuran\t','6 angsuran\t','12 angsuran') #bulan
#             bulan3 = 90 #hari
#             user1 = input('masukana lama pembayarannya : ')
#             if user1 =='3' :
#                 # Bunga = (lambda choise1,bulan3 : (choise1+choise1*0.5)/bulan3)(choise1,bulan3)
#                 print('jumlah yang harus dibayarkan setiap bulan adalah : ', 'Rp',round(fBunga(choise1, bulan3),3), 'dan angsuran selama : ', bulan3, 'hari(3 bulan)')
#             elif user1 =='6': 
#                 bulan6 = 180 #hari
#                 # Bunga = (lambda choise1,bulan6 : (choise1+choise1*0.5)/bulan6)(choise1,bulan6)
#                 print('jumlah yang harus dibayarkan setiap bulan adalah : ', 'Rp',round(fBunga(choise1, bulan6),3), 'dan angsuran selama : ', bulan6, 'hari(6 bulan)')
#             elif user1 =='12' :
#                 bulan12 = 365 #hari
#                 # Bunga = (lambda choise1,bulan12 : (choise1+choise1*0.5)/bulan12)(choise1,bulan12)
#                 print('jumlah yang harus dibayarkan setiap bulan adalah : ', 'Rp',round(fBunga(choise1, bulan12),3), 'dan angsuran selama : ', bulan12, 'hari(12 bulan)')
    
#     elif user == '2' :
#             print('3 angsuran\t','6 angsuran\t','12 angsuran') #bulan
#             bulan3 = 90 #hari
#             user1 = input('masukana lama pembayarannya : ')
#             if user1 =='3' :
#                 Bunga = (lambda choise2,bulan3 : (choise2+choise2*0.5)/bulan3)(choise2,bulan3)
#                 print('jumlah yang harus dibayarkan setiap bulan adalah : ', 'Rp',round(Bunga,3), 'dan angsuran selama : ', bulan3, 'hari(3 bulan)')
#             elif user1 =='6': 
#                 bulan6 = 180 #hari
#                 Bunga = (lambda choise2,bulan6 : (choise2+choise2*0.5)/bulan6)(choise2,bulan6)
#                 print('jumlah yang harus dibayarkan setiap bulan adalah : ', 'Rp',round(Bunga,3), 'dan angsuran selama : ', bulan6, 'hari(6 bulan)')
#             elif user1 =='12' :
#                 bulan12 = 365 #hari
#                 Bunga = (lambda choise2,bulan12 : (choise2+choise2*0.5)/bulan12)(choise2,bulan12)
#                 print('jumlah yang harus dibayarkan setiap bulan adalah : ', 'Rp',round(Bunga,3), 'dan angsuran selama : ', bulan12, 'hari(12 bulan)')
#     elif user == '3' :
#             print('3 angsuran\t','6 angsuran\t','12 angsuran') #bulan
#             bulan3 = 90 #hari
#             user1 = input('masukana lama pembayarannya : ')
#             if user1 =='3' :
#                 Bunga = (lambda choise3,bulan3 : (choise3+choise3*0.5)/bulan3)(choise3,bulan3)
#                 print('jumlah yang harus dibayarkan setiap bulan adalah : ', 'Rp',round(Bunga,3), 'dan angsuran selama : ', bulan3, 'hari(3 bulan)')
#             elif user1 =='6': 
#                 bulan6 = 180 #hari
#                 Bunga = (lambda choise3,bulan6 : (choise3+choise3*0.5)/bulan6)(choise3,bulan6)
#                 print('jumlah yang harus dibayarkan setiap bulan adalah : ', 'Rp',round(Bunga,3), 'dan angsuran selama : ', bulan6, 'hari(6 bulan)')
#             elif user1 =='12' :
#                 bulan12 = 365 #hari
#                 Bunga = (lambda choise3,bulan12 : (choise3+choise3*0.5)/bulan12)(choise3,bulan12)
#                 print('jumlah yang harus dibayarkan setiap bulan adalah : ', 'Rp',round(Bunga,3), 'dan angsuran selama : ', bulan12, 'hari(12 bulan)')
    
#     # peminjaman = print(format(tanggal))

# def login ():
#     Batasan = 3
#     for j in range(Batasan) :
#         File_db = open('login.csv','r')
#         username = input('masukan username : ')
#         password = input('masukan password :')
#         berhasil = False
#         for i in File_db :
#             Xusername, Ypassword = i.split(",")
#             Ypassword = password.strip ()
#             if (username==Xusername) and (password == Ypassword ) :
#                 Berhasil = True
#                 print('Selamat Anda berhasil login ')
#                 pilihan()
#     else :
#         print('melebihi batas, silahkan buat akun terlebih dahulu')
#         daftar()

    
    
# def daftar ():
#     username = input('masukan username Anda : ')    
#     password = input('masukan password : ')
#     newdata = {"username" : username , "password" : password }
#     save(username, password)
#     print('Selamat Anda sudah terdaftar ')
#     pilihan()
#     os.system('cls')

# def save(Username,Passoword) :
#     with open('login.csv', 'a', newline = '') as File_Db :
#         File_Db.write("\n"+Username+ "," +Passoword )

# def menu () :
#     print('-'*50)
#     print('\t\t SELAMAT DATANG DI UANGKU')
#     print('-'*50)
#     print('1. Login')
#     print('2. Daftar')
#     user = input('masukan menu : ')
#         # expr1 if condition1 else expr2 if condition2 else expr (For writing if-elif-else in one line in python we use the ternary operator.)
#     sukses = (login() if user =='1' else daftar() if user =='2' else menu() ) #contoh flow control 
#     # if user == '1':
#     #     login()
#     # else :
#     #     if user =='2' :
#     #         daftar()
#     #     else : 
#     #         menu()
# menu()
import os,time,pandas,csv,functools
from datetime import datetime

# a = [1, 2, 3, 4]
# sum_a = reduce(lambda x, y:x+y, a)
# print(sum_a)

#kekurangan :
#1. data admin ==> database admin, dan nanti admin bisa ngefilter sesuai keinginan dan sum total peminjamna (di menu_awal pilihan dan buat databasenya)


waktu = datetime.now()
hari = waktu.day
bulan = waktu.month
tahun = waktu.year
tanggal="{}/{}/{}".format(hari,bulan,tahun)

#Meriview materi cvs metode read 
# with open('login_user.csv','r')as logincsv :
#     reader = csv.DictReader(logincsv)
#     for row in reader:
#         print(row)

#admin
def admin_Login():
    admin = []
    with open ('admin.csv') as adm:
        admn = csv.reader(adm)
        for i in admn:
            admin.append(i)
    user_admin = input('masukan user admin : ')
    password_admin = input('masukan password admin : ')
    menu_admin()if [user_admin,password_admin] in admin else admin_Login()



def menu_admin():
    print('-'*36)
    print('\t\t MENU Admin')
    print('-'*36)
    print('\t1. Data Peminjaman')
    print('\t2. Data Pengguna')
    print('\t3. Data Admin')
    # statement1 if expression1 else (statement2 if expression2 else statement3)
    choice = input('Menu pilihan : ')
    # tes = (data_Peminjam)if choice =='1'  else ((data_pengguna) if choice =='2'  else menu_admin(name))  (data_admin) if choice =='3' else (menu_admin(name))
    tes = (data_Peminjam ())if choice =='1'  else ((data_pengguna ()) if choice =='2'  else menu_admin()) 
 
    

def data_Peminjam () :
    # with open('database.csv') as db :
    #     db = csv.reader(dbfile)
    #     all_rows = []
    #     for row in reader:
    #         all_rows.append(row)
    #         print(all_rows)

    data = [{'nasabah': 'Rizky', 'tanggal lahir': '14-12-2002', 'alamat': 'Jember','deposit' : 500000,'tanggal depo' :'1-1-2022','angsuran ' : 3},
         {'nasabah': 'Farid', 'tanggal lahir': '27-10-2002', 'alamat': 'Jember','deposit' : 1000000,'tanggal depo' : '01-3-2022','angsuran ' : 6},
         {'nasabah': 'Rahyan', 'tanggal lahir': '12-4-1998', 'alamat': 'Jember','deposit' : 2000000,'tanggal depo' :'01-3-2022' ,'angsuran ' : 3},
         {'nasabah': 'Hefilia', 'tanggal lahir': '12-5-2002', 'alamat': 'Surabaya','deposit' : 1000000,'tanggal depo' :'02-3-2022' ,'angsuran ' : 3},
         {'nasabah': 'Adrian', 'tanggal lahir': '12-4-1998', 'alamat': 'Malang','deposit' : 1000000,'tanggal depo' :'02-3-2022' ,'angsuran ' : 6},
         {'nasabah': 'Raka', 'tanggal lahir': '12-4-1998', 'alamat': 'Sidoarjo','deposit' : 2000000,'tanggal depo' :'01-3-2022' ,'angsuran ' : 6},
         {'nasabah': 'Dony', 'tanggal lahir': '12-4-1998', 'alamat': 'Bondowoso','deposit' : 2000000,'tanggal depo' :'07-3-2022' ,'angsuran ' : 3},
         {'nasabah': 'Gathan', 'tanggal lahir': '12-4-1998', 'alamat': 'Situbondo','deposit' : 500000,'tanggal depo' :'08-3-2022' ,'angsuran ' : 6},
         {'nasabah': 'Tisna', 'tanggal lahir': '12-4-1998', 'alamat': 'Surabya','deposit' : 500000,'tanggal depo' :'10-3-2022' ,'angsuran ' : 12},
         ]
    df = pandas.DataFrame(data)
    print(df)

    deposit = [datas for datas in data if datas['deposit']<2000000] #proses filtering menggunakan List Comprehension
    print(f'berikut ini data yang sudah di filter dengan deposit yang kurang dari 2 jt : \n ',deposit,{'nasabah'},{'deposit'})

    deposit =sum (datas ['deposit']for datas in data)
    print('total uang yang dipinjamkan kepada nasabah : ','Rp', deposit)

def data_pengguna():
      data = [
            {'username ': 'reza','umur': 20},
            {'username ': 'rendra','umur': 32},
            {'username ': 'reo','umur': 30},
            {'username ': 'nafiz','umur': 35},
            {'username ': 'donny','umur': 40},
            {'username ': 'farhan','umur': 30},
         ]
      df = pandas.DataFrame(data)
      print(df)

      username =sum(datas ['umur'/2]for datas in data)
      print('total pengguna aplikasi uangku  : ', username,{'umur'})


#User
#1.main program user
def pinjam (): 
    Bunga = (lambda x,y : x*0,5/y)
def pilihan (): #harus dibenerin 
    print('NB : Bunga cuma 5% dan sudah termasuk biaya admin\n')
    print('NO |\tPeminjaman        |')
    print ('1\t', 500000) 
    choise1 = 500000
    print('2\t',1000000)
    choise2=1000000
    print ('3\t',1500000)
    choise3=1500000
    print ('4\t',2000000)
    choise3=2000000
    user = (input('masukan pilihan : '))
    if user == '1' :
            print('3 angsuran\t','6 angsuran\t','12 angsuran') #bulan
            bulan3 = 90 #hari
            user1 = input('masukana lama pembayarannya : ')
            if user1 =='3' :
                Bunga = (lambda choise1,bulan3 : (choise1+choise1*0.5)/bulan3)(choise1,bulan3)
                print('jumlah yang harus dibayarkan setiap bulan adalah : ', 'Rp',round(Bunga,3), 'dan angsuran selama : ', bulan3, 'hari(3 bulan)')
            elif user1 =='6': 
                bulan6 = 180 #hari
                Bunga = (lambda choise1,bulan6 : (choise1+choise1*0.5)/bulan6)(choise1,bulan6)
                print('jumlah yang harus dibayarkan setiap bulan adalah : ', 'Rp',round(Bunga,3), 'dan angsuran selama : ', bulan6, 'hari(6 bulan)')
            elif user1 =='12' :
                bulan12 = 365 #hari
                Bunga = (lambda choise1,bulan12 : (choise1+choise1*0.5)/bulan12)(choise1,bulan12)
                print('jumlah yang harus dibayarkan setiap bulan adalah : ', 'Rp',round(Bunga,3), 'dan angsuran selama : ', bulan12, 'hari(12 bulan)')
    elif user == '2' :
            print('3 angsuran\t','6 angsuran\t','12 angsuran') #bulan
            bulan3 = 90 #hari
            user1 = input('masukana lama pembayarannya : ')
            if user1 =='3' :
                Bunga = (lambda choise2,bulan3 : (choise2+choise2*0.5)/bulan3)(choise2,bulan3)
                print('jumlah yang harus dibayarkan setiap bulan adalah : ', 'Rp',round(Bunga,3), 'dan angsuran selama : ', bulan3, 'hari(3 bulan)')
            elif user1 =='6': 
                bulan6 = 180 #hari
                Bunga = (lambda choise2,bulan6 : (choise2+choise2*0.5)/bulan6)(choise2,bulan6)
                print('jumlah yang harus dibayarkan setiap bulan adalah : ', 'Rp',round(Bunga,3), 'dan angsuran selama : ', bulan6, 'hari(6 bulan)')
            elif user1 =='12' :
                bulan12 = 365 #hari
                Bunga = (lambda choise2,bulan12 : (choise2+choise2*0.5)/bulan12)(choise2,bulan12)
                print('jumlah yang harus dibayarkan setiap bulan adalah : ', 'Rp',round(Bunga,3), 'dan angsuran selama : ', bulan12, 'hari(12 bulan)')
    elif user == '3' :
            print('3 angsuran\t','6 angsuran\t','12 angsuran') #bulan
            bulan3 = 90 #hari
            user1 = input('masukana lama pembayarannya : ')
            if user1 =='3' :
                Bunga = (lambda choise3,bulan3 : (choise3+choise3*0.5)/bulan3)(choise3,bulan3)
                print('jumlah yang harus dibayarkan setiap bulan adalah : ', 'Rp',round(Bunga,3), 'dan angsuran selama : ', bulan3, 'hari(3 bulan)')
            elif user1 =='6': 
                bulan6 = 180 #hari
                Bunga = (lambda choise3,bulan6 : (choise3+choise3*0.5)/bulan6)(choise3,bulan6)
                print('jumlah yang harus dibayarkan setiap bulan adalah : ', 'Rp',round(Bunga,3), 'dan angsuran selama : ', bulan6, 'hari(6 bulan)')
            elif user1 =='12' :
                bulan12 = 365 #hari
                Bunga = (lambda choise3,bulan12 : (choise3+choise3*0.5)/bulan12)(choise3,bulan12)
                print('jumlah yang harus dibayarkan setiap bulan adalah : ', 'Rp',round(Bunga,3), 'dan angsuran selama : ', bulan12, 'hari(12 bulan)')
    
#2. login and daftar user
def login_user (): #harus dibenerin
    Batasan = 3
    for j in range(Batasan) :
        File_db = open('login.csv','r')
        username = input('masukan username : ')
        password = input('masukan password :')
        berhasil = False
        for i in File_db :
            Xusername, Ypassword = i.split(",")
            Ypassword = password.strip ()
            if (username==Xusername) and (password == Ypassword ) :
                Berhasil = True
                print(f'Selamat Anda berhasil login' ,username,f'diakses pada ',tanggal)
                pilihan()
    else :
        print('melebihi batas, silahkan buat akun terlebih dahulu')
        daftar()    
def daftar ():
    username = input('masukan username Anda : ')    
    password = input('masukan password : ')
    newdata = {"username" : username , "password" : password }
    save(username, password)
    print('Selamat Anda sudah terdaftar ')
    pilihan()
    os.system('cls')

def save(Username,Passoword) :
    with open('login_user.csv', 'a', newline = '') as File_Db :
        File_Db.write("\n"+Username+ "," +Passoword )

def user_login() :
    print('-'*50)
    print('\tSELAMAT DATANG DI UANGKU (Halaman User)')
    print('-'*50)
    print('1. Login')
    print('2. Daftar')
    user = input('Pilih menu : ')
    sukses_user = (login_user() if user =='1'  else (daftar() if user =='2' else user()) )

def menu_awal () :
    print('-'*50)
    print('\t\t SELAMAT DATANG DI UANGKU')
    print('-'*50)
    print('1. Admin')
    print('2. User')
    user = input('masukan menu : ')
        # expr1 if condition1 else expr2 if condition2 else expr (For writing if-elif-else in one line in python we use the ternary operator.)
        #statement1 if expression1 else (statement2 if expression2 else statement3)
    sukses = (admin_Login() if user =='1'  else (user_login() if user =='2' else menu_awal()) ) #contoh flow control 
    # if user == '1':
    #     login_user()
    # else :
    #     if user =='2' :
    #         daftar()
    #     else : 
    #         menu_awal()
menu_awal()