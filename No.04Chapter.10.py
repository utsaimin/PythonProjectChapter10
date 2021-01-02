cariNIM = input('Masukkan  NIM yang dicari: ')

file = open('file2.txt', 'r')
data = file.readlines()
for i in range(len(data)):
    mahasiswa = data[i]
    nim, nama, alamat = mahasiswa.split('|')
    if cariNIM == nim :
        print('Data Mahasiswa')
        print('NIM    : ', nim, '\nNama   : ', nama,'\nAlamat : ', alamat)
        break
    else :
        break
if cariNIM not in nim:
    print('Data mahasiswa tidak ditemukan')
