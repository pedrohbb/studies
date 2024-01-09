#1
fruit = 'banana'
lenght = len(fruit)
index = -1

while index >= -lenght:
        letter = fruit[index]
        print(letter)
        index = index - 1

#1' travessia de string com for
fruit = 'banana'
for char in fruit:
    print(char)

#2
fruit = 'fruit'
#tudo
print(fruit[:])

#3
def count(x,y):
    count = 0
    for char in y:
        if x == char:
            count=count+1
    return count

prompt1 = input("Insira a palavra ou frase de interesse: \n")

prompt2 = input("Insira o caracter de interesse")

result = count(prompt1, prompt2)

print(f'O termo {prompt2} tem {result} caracteres do tipo {prompt1}.')

#4
word = 'banana'.s
count = word.count('a')
print(count)

#5
string = "X-DSPAM-Confidence:0.8475"

index = string.find(':')

result = float(string[index+1:])

print(result)

#6
#ok, já li