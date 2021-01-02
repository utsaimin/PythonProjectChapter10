file = open('file2.txt', 'r')
data = file.readlines()

dataMhs = {}
mahasiswa = []
for i in range(len(data)):
    mahasiswa = data[i].split()
    listMhs = {'nim' : mahasiswa[0], 'nama' : mahasiswa[1], 'alamat' : mahasiswa[2]}
    dataMhs = listMhs

    mahasiswa.append(dataMhs)
file.close()
print(dataMhs)
