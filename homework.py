desa = str(input('Desa : '))
no_kartu_keluarga = int(input('No Kartu Keluarga : '))
nik = int(input('Nomer Induk Kependudukan : '))
nama = str(input('Nama warga : '))
tempat_lahir = str(input('Tempat Lahir : '))
agama = str(input('Agama : '))
umur = int(input('Umur : '))
pekerjaan = str(input('Pekerjaan : '))
gaji_perbulan = int(input('Gaji perbulan : '))
jumlah_anak = int(input('Jumlah anak : '))

daftar_pekerjaan = ['Guru','Tni','Polisi']
hasil = 'mendapatkan bantuan pkh' if (pekerjaan not in daftar_pekerjaan and gaji_perbulan < 3000000 and umur >= 25 and jumlah_anak >= 1) else 'tidak mendapatkan bantuan pkh'
print(hasil)