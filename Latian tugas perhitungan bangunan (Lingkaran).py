# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 21:52:01 2022

@author: ASUS
"""

"Sistem Penilaian Sebuah Bangunan Lingkaran"

"""Deklarasi Variabel"""
nama        = input ("Masukkan Nama Bangunan      : ")
Pemilik     = input ("Masukkan Nama pemilik       : ")
alamat      = input ("Masukkan alamat bangunan    : ")

nil_π     = (3.14)
nil_r     = int(input ("Masukkan Nilai r²           : "))


""""""""""""""" Perhitungan """""""""""""""
rata = int(nil_π*nil_r*nil_r)



print("Nama         :", nama)
print("pemilik      :", Pemilik)
print("Alamat       :", alamat)

if (rata > 0) and (rata <=250):
    print("Nilai Luas Lingkaran Adalah",rata)
    print ("Luas Bangunannya kecil")
elif (rata >=251) and (rata <=500):
    print("Nilai Luas Lingkaran Adalah",rata)
    print ("Luas Bamgunannya Sedang")
elif (rata >=501) and (rata <=1000):
    print("Nilai Luas Lingkaran adalah",rata)
    print ("Luas Bangunannya Besar")
else:
    print("Nilai Luas Lingkaran",rata)
    print ("Mohon maaf Bangunan anda TIDAK LULUS uji coba")
