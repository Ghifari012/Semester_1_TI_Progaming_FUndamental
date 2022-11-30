# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 21:39:36 2022

@author: ASUS
"""

"""""Sistem Perhitungan Segitiga"""""


"""Deklarsi Variabel"""

nama    = input ("Masukkan Nama Bangunan    : ")
alamat  = input ("Masukkan Alamat Bangunan  : ")
pemilik = input ("Masukkan Nama Pemilik     : ")

nil_a = int (input ("Masukkan Nilai Alas : "))
nil_t = int (input ("Maskkan Nilai Tnggi : "))

"""Algoritma"""
rata = int (1/2*nil_a*nil_t)

if (rata >0) and (rata <=200):
    print ("Nilai Luas segitiga Adalah",rata)
    print ("Luas Bangunannya Kecil")
elif (rata >201) and (rata <=500):
    print ("Niaii  Luas Segitiga Adalah",rata)
    print ("Luas Bangunannya Sedang")
elif (rata >501) and (rata <=1000):
    print ("NIlai Luas Lingkaran Adalah", rata)
    print ("Las Bangunannya Besar")
else:
    print ("Nilai luas lingkaran Adalah", rata)
    print ("Mohon Maaf Bangunan Anda TIDAK LULUS Uji Coba")