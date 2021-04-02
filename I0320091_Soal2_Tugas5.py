#Soal 2
print("=======Membuat Program Grading Nilai=======")
print("==========Masukan Nama dan Nilai===========")
nama_siswa = input("Masukan Nama Siswa :")
nilai_siswa = float(input("Masukan Nilai Siswa :"))
if nilai_siswa < 60:
    print("Halo,", nama_siswa + "! Nilai anda setelah dikonversi adalah E")
elif nilai_siswa>= 60 and nilai_siswa <= 64:
    print("Halo,", nama_siswa + "! Nilai anda setelah dikonversi adalah C")
elif nilai_siswa >=65 and nilai_siswa <=69:
    print("Halo,", nama_siswa + "! Nilai anda setelah dikonversi adalah C+")
elif nilai_siswa >=70 and nilai_siswa <=74:
    print("Halo,", nama_siswa + "Nilai anda setelah dikonversi adalah B")
elif nilai_siswa >=75 and nilai_siswa <=79:
    print("Halo,", nama_siswa + "Nilai anda setelah dikonversi adalah B+")
elif nilai_siswa >=80 and nilai_siswa <= 84:
    print("Halo,", nama_siswa + "Nilai anda setelah dikonversi adalah A-")
elif nilai_siswa >=85 and nilai_siswa <= 100:
    print("Halo,", nama_siswa + "Nilai anda setelah dikonversi adalah A+")
else:
    print("nilai yang selain disebutkan tidak valid")