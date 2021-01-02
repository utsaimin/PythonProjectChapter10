nim = input('Masukkan NIM      : ')
nama = input('Masukkan Nama Mhs : ')
alamat = input('Masukkan Alamat   : ')
print('')

teks = ("{} | {} | {} \n".format(nim, nama, alamat))
data = open('file2.txt', 'w')
data.write(teks)
data.close()
tanya = input("Ulangi input lagi? (y/n) ")
print('')

while tanya == 'y' :
    nim = input('Masukkan NIM      : ')
    nama = input('Masukkan Nama Mhs : ')
    alamat = input('Masukkan Alamat   : ')
    print('')
    teks = ("{} | {} | {} \n".format(nim, nama, alamat))
    data = open('file2.txt', 'a')
    data.write(teks)
    data.close()
    tanya = input("Ulangi input lagi? (y/n) ")
    print('')
    if tanya == 'n':
        break
