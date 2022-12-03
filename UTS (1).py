# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:34:18 2022

@author: ASUS
"""

#HALAMAN UTAMA
print(('''--------------------------------------------
               HALAMAN APLIKASI SEDERHANA
    ---------------------------------------------------
    MENU YANG TERSEDIA
    1. PENGGAJIAN KARYAWAN
    2. EXIT
    ---------------------------------------------------
    '''))

#INPUTAN
menu = int(input("Pilih Menu yang tersedia :"))
if (menu == 1):
    print('''          ----------------------------------------------
          DATA GAJI PERUSAHAAN
          ----------------------------------------------
          ''')

print('''KODE DIVISI            NAMA DIVISI
10                : Pengembangan Sumber Daya Manusia
20                : Teknologi informasi
30                : Pemasaran
40                : Produksi


''')
print('''KODE JABATAN           NAMA JABATAN
240               : Kepala Divisi
110               : Kepala Sub Divisi
100               : Karyawan





''')
print(''''Masukkan Data Anda
      
      
      ''')  
NIK     = input("NIK                :")
Nama    = input("Nama lengkap       :")
Jenis_k = input("Jenis Kelamin      :")
Alamat  = input("Alamat Lengkap     :")
Kode_Div= input("Kode Divisi        :")
Kode_Jab= input("Kode Jabatan       :")

if(Kode_Div == "10"):
    Divisi = "Pengembangan Sumber Daya Manusia"
    
elif(Kode_Div == "20"):
    Divisi = "Teknologi Informasi"
    
elif(Kode_Div == "30"):
    Divisi = "Pemasaran"

elif(Kode_Div == "40"):
    Divisi = "Produksi"
else:
    Divisi = "Maaf Keyboard ang Anda Masukkan Salah"

 
if(Kode_Jab == "240"):
    jaba = "Kepala Divisi"
    Gaji = 5000000
    Tunjangan = 4000000
    pph21   = 250000
    bpjs_k  = 200000
    bpjs_t  = 150000
    Gaji_Bersih = Gaji+Tunjangan-pph21-bpjs_k-bpjs_t
    
elif(Kode_Jab == "110"):
    jaba = "Kepala Divisi"
    Gaji = 3000000
    Tunjangan = 4000000
    pph21   = 250000
    bpjs_k  = 200000
    bpjs_t  = 150000
    Gaji_Bersih = Gaji+Tunjangan-pph21-bpjs_k-bpjs_t
   
elif(Kode_Jab == "100"):
    jaba= "Karyawan"
    Gaji = 2500000
    Tunjangan = 4000000
    pph21   = 250000
    bpjs_k  = 200000
    bpjs_t  = 150000
    Gaji_Bersih = Gaji+Tunjangan-pph21-bpjs_k-bpjs_t
    
else:
    print("Maaf Kode Yang anda masukkan tidak tersedia")
    

    
#CETAK HASIL
print("---------------------------------------------------------")
print("                 HASIL PENGGAJIAN                        ")
print("---------------------------------------------------------")
print("NIK                           :", NIK)
print("Nama Lengkap                  :", Nama)
print("Jenis Kelamin                 :", Jenis_k)
print("Jabatan                       :", jaba)
print("Nama Divisi                   :", Divisi)
print("Alamat Lengkap                :", Alamat)
print("Gaji Pokok                    :", Gaji)
print("Tunjangan                     :", Tunjangan)
print("Pph21 (%5)                    :", pph21)
print("BPJS Kesehatan (%4)           :", bpjs_k)
print("BPJS Tenaga Kerja (%3)        :", bpjs_t)
print("Gaji Bersih                   :", Gaji_Bersih)
print("----------------------------------------------------------")