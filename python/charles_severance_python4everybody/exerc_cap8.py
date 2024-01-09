#1
def chop(x):
    x = x[1:]

def middle(x):
    x = x[1:-1]
    return x

x = [1,2,3,4]
y = chop(x)
z = middle(x)

print(x,y,z)

#2
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[2])
#resposta: é possível escrever uma linha que começa com 'From' e mais nada. dessa maneira não words[2] não existe e o programa retorna erro.
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) < 2 : continue
    if words[0] != 'From' : continue
    print(words[2])
#ainda aqui podem vir coisas sem sentido, como frases que fogem ao padrão, mas não haverá erro.

#3
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) >= 2 and words[0] == 'From':
        print(words[2])
    continue

#4
fhand = open('romeo.txt')
count = 0
words_text = []

for line in fhand:
    listinha = line.split()
    for word in listinha:
        if word in words_text:
            continue
        else: 
            words_text.append(word)

words_text.sort()

print(words_text)

#5
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From '):
        print(line.split()[1])
        count += 1
print(f'Foram enviados {count} emails')

#6
numbers_list = []
count = 0
soma = 0

while True:
    count2 = count + 1
    prompt1 = input(f'Insira o {count2}º número ou "done" para encerrar a lista')

    if prompt1 == 'done':
        break    

    else:
        numbers_list.append(float(prompt1))
        soma += float(prompt1)
        count += 1

    
max_numb = max(numbers_list)
min_numb = min(numbers_list)

print(f'Maximum: {max_numb};\nMinimum: {min_numb};')

if count > 0:
    aver_numb = soma/count
    print(f'Soma: {soma};\nAverage: {aver_numb}')
else:
    print("Nenhum número informado")



    
    

    

