data = open('D:/teks05.txt', 'r')
result = []

for x in data.readlines() :
    if('\n' in x) :
        
        replaced = x.replace('\n','')
        splitted = replaced.split('|')
        valueList = int(splitted[0]) + int(splitted[1])
        result.append(valueList)
        
    else :
        
        splitted = x.split('|')
        valueList = int(splitted[0]) + int(splitted[1])
        result.append(valueList)
data.close()
output = open('D:/hasilTeks05.txt', 'w')

for x in range(len(result)) :
    output.write(str(result[x]) + '\n')

output.close()
print(hasil)
