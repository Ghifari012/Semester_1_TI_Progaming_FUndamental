# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 13:19:46 2022

@author: ASUS
"""

print(('''--------------------------------------------------------------------
               HALAMAN UTAMA KALKULATOR SEDERHANA
--------------------------------------------------------------------
MENU YANG TERSEDIA
1. JADWAL UJIAN AKHIR SEMESTER
2. CETAK HASIL UJIAN AKHIR SEMESTER
3. EXIT
--------------------------------------------------------------------
    '''))

#pilihan Menu
menu = int(input("Pilih Menu       :"))

#Kondisi
if (menu == 2):
        print('''------------------------------------------------------------
              HALAMAN CETAK HASIL UAS
-----------------------------------------------------------------------------
                1.Cetak hasil
                2.Kembali
------------------------------------------------------
                ''')
                
#inputan
NIM     = input("Masukkan NIM anda                 :")
Nama    = input("Masukkan Nama lengkap anda        :")
Jenis_k = input("Masukkan Jenis Kelamin anda       :")
Alamat  = input("Masukkan Alamat Lengkap anda      :")
print ("================================================================")
print("Masukkan NILAI anda")

#Inputan
if(NIM [0:1] =="1"):
   Div = "D3 KEPERAWATAN"
   b_indo = int(input("Bahasa Indonesia  :"))
   agama = int(input("Agama             :"))
   pancasila = int(input("Pancasila         :"))
   bio = int(input("Biokimia            :"))
   fisika = int(input("Fisika            :"))
   psiko = int(input("Psikologi             :"))
   ibd = int(input("IBD                 :"))
   gizi = int(input("Gizi                   :"))
   kdk = int(input("KDK                 :"))
   etika = int(input("Etika Keperawtan   :"))
   rata = int((b_indo+agama+pancasila+bio+fisika+psiko+ibd+gizi+kdk+etika)/10)
   
   if(NIM [1:5] == "2400"):
    status = "mahasiswa reguler"
   if(NIM [1:5] == "2500"):
    status = "kelas karyawan"
  
#perhitungan    
   if(b_indo >= 81)and (b_indo <=100):
       grade = "A"
   elif(b_indo >= 70) and (b_indo <=80):
      grade = "B"
   else:
      grade = "C"
      
   if(agama >= 81)and (agama <= 100):
      grade1 = "A"
   elif(agama >=70)and (agama <= 80):
     grade1 = "B"
   else:
     grade1 = "C"            

   if(pancasila >= 81)and (pancasila <=100):
      grade2 = "A"
   elif(pancasila >=70)and (pancasila <= 80):
      grade2 = "B"
   else:
     grade2 = "C"
    
   if(bio <= 100)and (bio >=81):
     grade3 = "A"
   elif(bio <=80)and (bio >= 70):
     grade3 = "B"
   else:
     grade3 = "C"
     
   if(fisika >= 81) and (fisika <= 100):
     grade4 = "A"
   elif(fisika >=70)and (fisika <=80):
    grade4 = "B"
   else:
    grade4 = "C"

   if(psiko >= 81) and (psiko <= 100):
     grade5 = "A"
   elif(psiko >=70)and (psiko <= 80):
    grade5 = "B"
   else:
    grade5 = "C"
    
   if(ibd >= 81)and (ibd <= 100):
     grade6 = "A"
   elif(ibd >=70)and (ibd <= 80):
    grade6 = "B"
   else:
    grade6 = "C"

   if(gizi >= 81) and (gizi <=100):
     grade7 = "A"
   elif(gizi >=70)and (gizi <= 80):
    grade7 = "B"
   else:
    grade7 = "C"
    
    
   if(kdk >= 81)and (kdk <=100):
      grade8 = "A"
   elif(kdk >=70)and (kdk <= 80):
     grade8 = "B"
   else:
     grade8 = "C"
     
   if(etika >= 81)and (etika <=100):
       grade9 = "A"
   elif(etika >=70)and (etika <= 80):
      grade9 = "B"
   else:
      grade9 = "C"
      
   if(rata >= 81)and (rata <=100):
        grade_1 = "A"
   elif(rata >=70)and (rata <= 80):
       grade_1 = "B"
   else:
       grade_1 = "C"
       
#hasilcetak
print("---------------------------------------------------------")
print("            HASIL UJIAN AKHIR SEMESTER                   ")
print("---------------------------------------------------------")
print("NIM                           :", NIM)
print("Nama Lengkap                  :", Nama)
print("Jenis Kelamin                 :", Jenis_k)
print("Program studi                 :", Div)
print("Alamat Lengkap                :", Alamat)
print("Status                        :", status)
print("----------------------------------------------------------------------")
print("MATA KULIAH\t\t\t\t\t\t\t\tNilai/grade")
print("----------------------------------------------------------------------")
print("Bahasa INdonesia\t\t\t\t\t\t:",b_indo,grade)
print("Agama\t\t\t\t\t\t\t:",agama, grade1)
print("Pancasila\t\t\t\t\t\t:",pancasila,grade2)
print("Biokimia\t\t\t\t:",bio, grade3)
print("Fisika\t\t\t\t\t\t\t:",fisika, grade4)
print("Psikologi\t\t\t\t\t:",psiko, grade5)
print("Ilmu Biomedik Dasae\t\t\t\t:",ibd,grade6)
print("Gizi:",gizi, grade7)
print("KDK\t:",kdk, grade8)
print("Etika Keperawatan\t:",etika, grade9)
print("rata rata\t\t\t\t\t\t\t\t:", rata, grade_1)
      
      
if(NIM [0:1] =="2"):
   Div = "S1 GIZI"
   b_indo = int(input("Bahasa Indonesia :"))
   agama = int(input("Agama             :"))
   pancasila = int(input("Pancasila     :"))
   bio = int(input("Biologi         :"))
   sos = int(input("Sosiologi & Antropologi Gizi        : "))
   kimi = int(input("Kimia      :"))
   mtk = int(input("Matematika   :"))
   ibd = int(input("Ilmu Gizi Dasar     :"))
   fisio = int(input("Anotomi Fisiologi     :"))
   kom = int(input("Komunikasi dan Psikologi    :"))
   rata = int((b_indo+agama+pancasila+bio+sos+kimi+mtk+ibd+fisio+kom)/10)
   
   if(NIM [1:5] == "2400"):
    status = "mahasiswa reguler"
   if(NIM [1:5] == "2500"):
    status = "kelas karyawan"
  
#perhitungan    
   if(b_indo >= 81)and (b_indo <=100):
       grade = "A"
   elif(b_indo >= 70) and (b_indo <=80):
      grade = "B"
   else:
      grade = "C"
      
   if(agama >= 81)and (agama <= 100):
      grade1 = "A"
   elif(agama >=70)and (agama <= 80):
     grade1 = "B"
   else:
     grade1 = "C"            

   if(pancasila >= 81)and (pancasila <=100):
      grade2 = "A"
   elif(pancasila >=70)and (pancasila <= 80):
      grade2 = "B"
   else:
     grade2 = "C"
    
   if(bio <= 100)and (bio >=81):
     grade3 = "A"
   elif(bio <=80)and (bio >= 70):
     grade3 = "B"
   else:
     grade3 = "C"
     
   if(sos >= 81) and (sos <= 100):
     grade4 = "A"
   elif(sos >=70)and (sos <=80):
    grade4 = "B"
   else:
    grade4 = "C"

   if(kimi >= 81) and (kimi <= 100):
     grade5 = "A"
   elif(kimi >=70)and (kimi <= 80):
    grade5 = "B"
   else:
    grade5 = "C"
    
   if(mtk >= 81)and (mtk <= 100):
     grade6 = "A"
   elif(mtk >=70)and (mtk <= 80):
    grade6 = "B"
   else:
    grade6 = "C"

   if(ibd >= 81) and (ibd <=100):
     grade7 = "A"
   elif(ibd >=70)and (ibd <= 80):
    grade7 = "B"
   else:
    grade7 = "C"
    
   if(fisio >= 81)and (fisio <=100):
     grade8 = "A"
   elif(fisio >=70)and (fisio <= 80):
    grade8 = "B"
   else:
    grade8 = "C"
    
    if(kom >= 81)and (kom <=100):
      grade9 = "A"
    elif(kom >=70)and (kom <= 80):
     grade9 = "B"
    else:
     grade9 = "C"
    
    if(rata >= 81)and (rata <=100):
      grade_1 = "A"
    elif(rata >=70)and (rata <= 80):
     grade_1 = "B"
    else:
     grade_1 = "C"
     
     
      
#hasilcetak
print("---------------------------------------------------------")
print("            HASIL UJIAN AKHIR SEMESTER                   ")
print("---------------------------------------------------------")
print("NIM                           :", NIM)
print("Nama Lengkap                  :", Nama)
print("Jenis Kelamin                 :", Jenis_k)
print("Nama Divisi                   :", Div)
print("Alamat Lengkap                :", Alamat)
print("Status                        :", status)
print("----------------------------------------------------------------------")
print("MATA KULIAH\t\t\t\t\t\t\t\tNilai/grade")
print("----------------------------------------------------------------------")
print("Bahasa INdonesia\t\t\t\t\t\t:",b_indo,grade)
print("Bahasa Agama\t\t\t\t\t\t\t:",agama, grade1)
print("Bahasa Pancasila\t\t\t\t\t\t:",pancasila,grade2)
print("Bahasa Biologi\t\t\t\t:",bio, grade3)
print("Bahasa Sosiologi & Antropologi Gizi \t\t\t\t\t\t\t:",sos, grade4)
print("Bahasa Kimia\t\t\t\t\t:",kimi, grade5)
print("Bahasa Matematika\t\t\t\t:",mtk,grade6)
print("Bahasa Ilmu Gizi Dasar\t:",ibd, grade7)
print("Bahasa Atonomi fisiologi\t:",fisio, grade8)
print("Bahasa Komunikasi & Psikologi\t:",kom, grade9)
print("rata rata\t\t\t\t\t\t\t\t:", rata, grade_1)

if(NIM [0:1] =="3"):
   Div = "S1 KEPERAWATAN"
   b_indo = int(input("Bahasa Indonesia :"))
   agama = int(input("Agama             :"))
   pancasila = int(input("Pancasila     :"))
   ibd = int(input("Ilmu Gizi Dasar     :"))
   pem_das = int(input("Pemunuhan Kebutuhan Dasar Manusia :"))
   konsep = int(input("Konsep Dasa Keperawatan :"))
   proses = int(input("Proses Keperawatan dan Berfikir Kritis :"))
   filsafah =int(input("Filsafah dan teori keperawatan :"))
   rata = int((b_indo+agama+pancasila+ibd+pem_das+konsep+proses+filsafah)/8)
   
   if(NIM [1:5] == "2400"):
    status = "mahasiswa reguler"
   if(NIM [1:5] == "2500"):
    status = "kelas karyawan"
  
#perhitungan    
   if(b_indo >= 81)and (b_indo <=100):
       grade = "A"
   elif(b_indo >= 70) and (b_indo <=80):
      grade = "B"
   else:
      grade = "C"
      
   if(agama >= 81)and (agama <= 100):
      grade1 = "A"
   elif(agama >=70)and (agama <= 80):
     grade1 = "B"
   else:
     grade1 = "C"            

   if(pancasila >= 81)and (pancasila <=100):
      grade2 = "A"
   elif(pancasila >=70)and (pancasila <= 80):
      grade2 = "B"
   else:
     grade2 = "C"
    
   if(ibd <= 100)and (ibd >=81):
     grade3 = "A"
   elif(ibd <=80)and (ibd >= 70):
     grade3 = "B"
   else:
     grade3 = "C"
     
   if(pem_das >= 81) and (pem_das <= 100):
     grade4 = "A"
   elif(pem_das >=70)and (pem_das <=80):
    grade4 = "B"
   else:
    grade4 = "C"

   if(konsep >= 81) and (konsep <= 100):
     grade5 = "A"
   elif(konsep >=70)and (konsep <= 80):
    grade5 = "B"
   else:
    grade5 = "C"
    
   if(proses >= 81)and (proses <= 100):
     grade6 = "A"
   elif(proses >=70)and (proses <= 80):
    grade6 = "B"
   else:
    grade6 = "C"

   if(filsafah >= 81) and (filsafah <=100):
     grade7 = "A"
   elif(filsafah >=70)and (filsafah <= 80):
    grade7 = "B"
   else:
    grade7 = "C"
  
    
    if(rata >= 81)and (rata <=100):
      grade_1 = "A"
    elif(rata >=70)and (rata <= 80):
     grade_1 = "B"
    else:
     grade_1 = "C"
     
     
      
#hasilcetak
print("---------------------------------------------------------")
print("            HASIL UJIAN AKHIR SEMESTER                   ")
print("---------------------------------------------------------")
print("NIM                           :", NIM)
print("Nama Lengkap                  :", Nama)
print("Jenis Kelamin                 :", Jenis_k)
print("Program Studi                 :", Div)
print("Alamat Lengkap                :", Alamat)
print("Status                        :", status)
print("----------------------------------------------------------------------")
print("MATA KULIAH\t\t\t\t\t\t\t\tNilai/grade")
print("----------------------------------------------------------------------")
print("Bahasa INdonesia\t\t\t\t\t\t:",b_indo,grade)
print("Bahasa Agama\t\t\t\t\t\t\t:",agama, grade1)
print("Bahasa Pancasila\t\t\t\t\t\t:",pancasila,grade2)
print("Bahasa Ilmu Biomedik Dasar\t\t\t\t:",ibd, grade3)
print("Bahasa Pemulihan Kebutuhan Dasar \t\t\t\t\t\t\t:",pem_das, grade4)
print("Bahasa Konsep Dasar Keperawtan\t\t\t\t\t:",konsep, grade5)
print("Bahasa Proses Keperawatan dan berfikir Kritis \t\t\t\t:",proses,grade6)
print("Bahasa Filsafah dan Teori Keperawatan\t:",filsafah, grade7)
print("rata rata\t\t\t\t\t\t\t\t:", rata, grade_1)
   
   
   
if(NIM [0:1] =="4"):
   Div = "S1 PENDIDIKAN BAHASA INGGRIS"
   b_indo = int(input("Bahasa Indonesia :"))
   agama = int(input("Agama             :"))
   pancasila = int(input("Pancasila     :"))
   lfl = int(input("Listening For Leisure :"))
   bes = int(input("Basic English Structure :"))
   lr = int(input("Literal Reading :"))
   free = int(input("free writing :"))
   vocab = int(input("Vocabulary :"))
   ikd = int(input("Ilmu Kealaman Dasar :"))
   p = int(input("Pronunciation :"))
   speak = int(input("Speaking for Daily Communication :"))
   rata = int((b_indo+agama+pancasila+bio+sos+kimi+mtk+ibd+fisio+kom)/10)

   if(NIM [1:5] == "2400"):
    status = "mahasiswa reguler"
   if(NIM [1:5] == "2500"):
    status = "kelas karyawan"
  
#perhitungan    
   if(b_indo >= 81)and (b_indo <=100):
       grade = "A"
   elif(b_indo >= 70) and (b_indo <=80):
      grade = "B"
   else:
      grade = "C"
      
   if(agama >= 81)and (agama <= 100):
      grade1 = "A"
   elif(agama >=70)and (agama <= 80):
     grade1 = "B"
   else:
     grade1 = "C"            

   if(pancasila >= 81)and (pancasila <=100):
      grade2 = "A"
   elif(pancasila >=70)and (pancasila <= 80):
      grade2 = "B"
   else:
     grade2 = "C"
    
   if(bio <= 100)and (bio >=81):
     grade3 = "A"
   elif(bio <=80)and (bio >= 70):
     grade3 = "B"
   else:
     grade3 = "C"
     
   if(sos >= 81) and (sos <= 100):
     grade4 = "A"
   elif(sos >=70)and (sos <=80):
    grade4 = "B"
   else:
    grade4 = "C"

   if(kimi >= 81) and (kimi <= 100):
     grade5 = "A"
   elif(kimi >=70)and (kimi <= 80):
    grade5 = "B"
   else:
    grade5 = "C"
    
   if(mtk >= 81)and (mtk <= 100):
     grade6 = "A"
   elif(mtk >=70)and (mtk <= 80):
    grade6 = "B"
   else:
    grade6 = "C"

   if(ibd >= 81) and (ibd <=100):
     grade7 = "A"
   elif(ibd >=70)and (ibd <= 80):
    grade7 = "B"
   else:
    grade7 = "C"
    
   if(fisio >= 81)and (fisio <=100):
     grade8 = "A"
   elif(fisio >=70)and (fisio <= 80):
    grade8 = "B"
   else:
    grade8 = "C"
    
    if(kom >= 81)and (kom <=100):
      grade9 = "A"
    elif(kom >=70)and (kom <= 80):
     grade9 = "B"
    else:
     grade9 = "C"
    
    if(rata >= 81)and (rata <=100):
      grade_1 = "A"
    elif(rata >=70)and (rata <= 80):
     grade_1 = "B"
    else:
     grade_1 = "C"
     
     
      
#hasilcetak
print("---------------------------------------------------------")
print("            HASIL UJIAN AKHIR SEMESTER                   ")
print("---------------------------------------------------------")
print("NIM                           :", NIM)
print("Nama Lengkap                  :", Nama)
print("Jenis Kelamin                 :", Jenis_k)
print("Nama Divisi                   :", Div)
print("Alamat Lengkap                :", Alamat)
print("Status                        :", status)
print("----------------------------------------------------------------------")
print("MATA KULIAH\t\t\t\t\t\t\t\tNilai/grade")
print("----------------------------------------------------------------------")
print("Bahasa INdonesia\t\t\t\t\t\t:",b_indo,grade)
print("Bahasa Agama\t\t\t\t\t\t\t:",agama, grade1)
print("Bahasa Pancasila\t\t\t\t\t\t:",pancasila,grade2)
print("Bahasa Biologi\t\t\t\t:",bio, grade3)
print("Bahasa Sosiologi & Antropologi Gizi \t\t\t\t\t\t\t:",sos, grade4)
print("Bahasa Kimia\t\t\t\t\t:",kimi, grade5)
print("Bahasa Matematika\t\t\t\t:",mtk,grade6)
print("Bahasa Ilmu Gizi Dasar\t:",ibd, grade7)
print("Bahasa Atonomi fisiologi\t:",fisio, grade8)
print("Bahasa Komunikasi & Psikologi\t:",kom, grade9)
print("rata rata\t\t\t\t\t\t\t\t:", rata, grade_1)
   
   
   
   
if(NIM [0:1] =="5"):
   Div = "S1 PENDIDIKAN GURU SD"
   b_indo = int(input("Bahasa Indonesia :"))
   agama = int(input("Agama             :"))
   pancasila = int(input("Pancasila     :"))
if(NIM [0:1] =="6"):
   Div = "S1 MANAJEMEN"
   b_indo = int(input("Bahasa Indonesia :"))
   agama = int(input("Agama             :"))
   pancasila = int(input("Pancasila     :"))
if(NIM [0:1] =="7"):
   Div = "S1 AKUNTANSI"
   b_indo = int(input("Bahasa Indonesia :"))
   agama = int(input("Agama             :"))
   pancasila = int(input("Pancasila     :"))
if(NIM [0:1] =="8"):
   Div = "S1 INFORMATIKA"
   b_indo = int(input("Bahasa INdonesia                 :"))
   agama = int(input("Agama                            :"))
   pancasila = int(input("Pncasila                         :"))
   login = int(input("Logika Informatika               :"))
   kalkulus = int(input("Kalkulus                         :"))
   sis_op = int(input("Sistem Operasi                   :"))
   dasar_pem = int(input("Dasar Pemrograman                :"))
   pti = int(input("Pengantar Teknologi Informasi    :"))
   rata = int((b_indo+agama+pancasila+login+kalkulus+sis_op+dasar_pem+pti)/8)
  
   if(NIM [1:5] == "2400"):
       status = "mahasiswa reguler"
   if(NIM [1:5] == "2500"):
       status = "kelas karyawan"
   
       
   if(b_indo >= 81)and (b_indo <=100):
       grade = "A"
   elif(b_indo >= 70) and (b_indo <=80):
      grade = "B"
   else:
      grade = "C"
      
   if(agama >= 81)and (agama <= 100):
      grade1 = "A"
   elif(agama >=70)and (agama <= 80):
     grade1 = "B"
   else:
     grade1 = "C"            

   if(pancasila >= 81)and (pancasila <=100):
      grade2 = "A"
   elif(pancasila >=70)and (pancasila <= 80):
      grade2 = "B"
   else:
     grade2 = "C"
    
   if(login <= 100)and (login >=81):
     grade3 = "A"
   elif(login <=80)and (login >= 70):
     grade3 = "B"
   else:
     grade3 = "C"
     
   if(kalkulus >= 81) and (kalkulus <= 100):
     grade4 = "A"
   elif(kalkulus >=70)and (kalkulus <=80):
    grade4 = "B"
   else:
    grade4 = "C"

   if(sis_op >= 81) and (sis_op <= 100):
     grade5 = "A"
   elif(sis_op >=70)and (sis_op <= 80):
    grade5 = "B"
   else:
    grade5 = "C"
    
   if(dasar_pem >= 81)and (dasar_pem <= 100):
     grade6 = "A"
   elif(dasar_pem >=70)and (dasar_pem <= 80):
    grade6 = "B"
   else:
    grade6 = "C"

   if(pti >= 81) and (pti <=100):
     grade7 = "A"
   elif(pti >=70)and (pti <= 80):
    grade7 = "B"
   else:
    grade7 = "C"
    
   if(rata >= 81)and (rata <=100):
     grade_1 = "A"
   elif(rata >=70)and (rata <= 80):
    grade_1 = "B"
   else:
    grade_1 = "C"
    
print("---------------------------------------------------------")
print("            HASIL UJIAN AKHIR SEMESTER                   ")
print("---------------------------------------------------------")
print("NIM                           :", NIM)
print("Nama Lengkap                  :", Nama)
print("Jenis Kelamin                 :", Jenis_k)
print("Nama Divisi                   :", Div)
print("Alamat Lengkap                :", Alamat)
print("Status                        :", status)
print("----------------------------------------------------------------------")
print("MATA KULIAH\t\t\t\t\t\t\t\tNilai\t\t\t\t\tgrade")
print("----------------------------------------------------------------------")
print("Bahasa INdonesia\t\t\t\t\t\t:",b_indo, grade)
print("Bahasa Agama\t\t\t\t\t\t\t:",agama, grade1)
print("Bahasa Pancasila\t\t\t\t\t\t:",pancasila,grade2)
print("Bahasa logika Informatika\t\t\t\t:",login, grade3)
print("Bahasa Kalkulus\t\t\t\t\t\t\t:",kalkulus, grade4)
print("Bahasa Sistem Operasi\t\t\t\t\t:",sis_op, grade5)
print("Bahasa Dasar Pemrograman\t\t\t\t:",dasar_pem,grade6)
print("Bahasa Pengantar Teknologi Informasi\t:",pti, grade7)
print("rata rata\t\t\t\t\t\t\t\t:", rata, grade_1)

  


if(NIM [0:1] =="9"):
   Div = "S1 HUKUM"
   b_indo = int(input("Bahasa INdonesia     :"))
   agama = int(input("Agama                 :"))
   pancasila = int(input("Pancasila         :"))
            
if(NIM [1:5] == "2400"):
    status = "mahasiswa reguler"
if(NIM [1:5] == "2500"):
    status = "kelas karyawan"
else: 
    status = "Maaf Keyboard ang Anda Masukkan Salah"