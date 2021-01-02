def sandiCaesar(data, key):
    hasil = ''
    file = open(data, 'r')
    for i in file.read():
        if i == ' ':
            hasil += i
        elif i.islower():
            hasil += chr((ord(i) + key - 97) % 26 + 97)
        else:
            hasil += chr((ord(i) + key - 65) % 26 + 65)
    file.close()
    f_Deskrip = open(data + '.decrypt', 'w')
    f_Deskrip.write(hasil)
    f_Deskrip.close()
    print('File dekripsi : {}.decrypt'.format(data))

data = input('Nama file yang ingin di dekripsi : ')
key = int(input('Input Keyword : '))
sandiCaesar(data, key)
