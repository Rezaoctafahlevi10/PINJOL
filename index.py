import csv
from datetime import datetime
import os
import time
from  functools import reduce
# a = [1, 2, 3, 4]
# sum_a = reduce(lambda x, y:x+y, a)
# print(sum_a)

#kekurangan :
#1. data admin ==> database admin, dan nanti admin bisa ngefilter sesuai keinginan dan sum total peminjamna (di menu pilihan dan buat databasenya)


waktu = datetime.now()
hari = waktu.day
bulan = waktu.month
tahun = waktu.year
tanggal="{}/{}/{}".format(hari,bulan,tahun)

#Meriview materi cvs metode read 
# with open('login.csv','r')as logincsv :
#     reader = csv.DictReader(logincsv)
#     for row in reader:
#         print(row)

# def pinjam (): 
#     Bunga = (lambda x,y : x*0,5/y)
def pilihan ():
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
    
    # peminjaman = print(format(tanggal))

def login ():
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
                print('Selamat Anda berhasil login ')
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
    with open('login.csv', 'a', newline = '') as File_Db :
        File_Db.write("\n"+Username+ "," +Passoword )

def menu () :
    print('-'*50)
    print('\t\t SELAMAT DATANG DI UANGKU')
    print('-'*50)
    print('1. Login')
    print('2. Daftar')
    user = input('masukan menu : ')
        # expr1 if condition1 else expr2 if condition2 else expr (For writing if-elif-else in one line in python we use the ternary operator.)
    sukses = (login() if user =='1' else daftar() if user =='2' else menu() ) #contoh flow control 
    # if user == '1':
    #     login()
    # else :
    #     if user =='2' :
    #         daftar()
    #     else : 
    #         menu()
menu()

