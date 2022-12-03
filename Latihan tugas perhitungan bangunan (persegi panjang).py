""" Sistem Penilaian Sebuah Persegi Panjang """

"""Deklarasi Variabel"""
nama        = input ("Masukkan Nama Bangunan      : ")
Pemilik     = input ("Masukkan Nama pemilik       : ")
alamat      = input ("Masukkan alamat bangunan    : ")

nil_panjang     = int(input ("Masukkan Nilai Panjang      : "))
nil_lebar       = int(input ("Masukkan Nilai lebar        : "))


""""""""""""""" Perhitungan """""""""""""""
rata = int(nil_panjang*nil_lebar)



print("Nama         :", nama)
print("pemilik      :", Pemilik)
print("Alamat       :", alamat)

if (rata > 0) and (rata <=250):
    print("Nilai Luas Persegi Panjang Adalah",rata)
    print ("Luas Bangunannya kecil")
elif (rata >=251) and (rata <=500):
    print("Nilai Luas persegi panjang Adalah",rata)
    print ("Luas Bamgunannya Sedang")
elif (rata >=501) and (rata <=1000):
    print("Nilai Luas Persegi Panjang adalah",rata)
    print ("Luas Bangunannya Besar")
else:
    print("Nilai Luas Persegi Panjang",rata)
    print ("Mohon maaf Bangunan anda TIDAK LULUS uji coba") 
