#Soal 1
print("==========Progam Untuk Menyapa Pengunjung==========")
print("==========Masukan Nama dan Jenis Kelamin===========")
nama_pengunjung = input("Masukan Nama Pengunjung :")
jenis_kelamin_pengunjung = input("Masukan Jenis Kelamin Pengunjung :")
if (jenis_kelamin_pengunjung == 'Perempuan'):
    print("Selamat datang, Nyonya,", nama_pengunjung, "!")
else:
    print("Selamat datang, Tuan", nama_pengunjung, "!")
print()