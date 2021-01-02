myfile = open('d:\file1.txt', 'r')

baris = myfile.readlines()

genap = []
ganjil = []

for i in range(len(baris)):
    angka = baris[i].replace('\n','')
    if (int(angka)%2)==0:
        genap.append(baris[i])
    else :
        ganjil.append(baris[i])
print('Banyaknya bilangan genap : ', len(genap))
print('Banyaknya bilangan ganjil : ', len(ganjil))
