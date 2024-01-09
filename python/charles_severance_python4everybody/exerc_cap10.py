#1
addr_dict = {}
fhand = open(input("Enter the file name: "))

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        if words[1] not in addr_dict:
            addr_dict[words[1]] = 1
        else:
            addr_dict[words[1]] += 1
    mailfreq_tup = list(addr_dict.items())

print(sorted(mailfreq_tup, key = lambda x: x[1], reverse = True)[0][0], sorted(mailfreq_tup, key = lambda x: x[1], reverse = True)[0][1])

#2
hour_dict = {}
fhand = open(input("Enter the file name: "))

for line in fhand:
    if line.startswith('From '):
        words = line.split(':')
        hours = words[0][-2:]
        if hours not in hour_dict:
            hour_dict[hours] = 1
        else:
            hour_dict[hours] += 1
    mailfreq_tup = list(hour_dict.items())

for m,n in sorted(mailfreq_tup, key = lambda x: x[1], reverse = True): 
    print(f'Horário: {m} horas. Quantidade de msgs: {n}')

#3
letters_dict = {}
alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','x','z')
fhand = open(input("Enter the file name: "))

for line in fhand:
    line_list = line.lower().split()
    for word in line_list:
        for charact in word:
            if charact not in alphabet:
                continue
            else:
                if charact not in letters_dict:
                    letters_dict[charact] = 1
                else: 
                    letters_dict[charact] += 1

total = sum(list(letters_dict.values()))
letter_rate = []
letterfreqord_tup = list(sorted(letters_dict.items(), key = lambda x: x[0]))

print(f'Total de Letras: {total}')

for m,n in letterfreqord_tup: 
    print(f'Letra: {m}. Quantidade de ocorrências: {n}. Frequência relativa: {round(n*100/total,2)}%')
