#1
fhand = open('mbox-short.txt')
for line in fhand:
    print((line[:-1]).upper())

#2
fhand = open(input("Insira o nome do arquivo: "))

count = 0
soma = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        print(line[20:26])
        spam = float(line[20:26])
        count += 1
        soma += spam
        
print(f'Spam average: soma/count')

#3
try:
    count = 0
    arcname = input("Insira o nome do arquivo: ")
    fhand = open(arcname)
    for line in fhand:
        count += 1
    print(count)
except:
    if arcname == 'Shazam!':
        print('Shazam is a great hero')
    else:
        print('Erro: arquivo inexistente')


