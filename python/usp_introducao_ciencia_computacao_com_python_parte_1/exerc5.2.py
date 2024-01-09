# Exercício 2 - Primos
# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função
# Exemplos de execução no shell do Python:
# >>> maior_primo(100)
# 97
# >>> maior_primo(7)
# 7
def éPrimo(x):
    y = int(x**(1/2))
    if y >= 2:
        prim = True
        for i in range(2, y+1):
            if (x % i) == 0:
                prim = False
                break
        if prim == True:
            return x
                 

def maior_primo(x):
    A = []
    for i in range(2, x+1):
        if éPrimo(i) != None:
            A.append(éPrimo(i))
    maximum = max(A)
    return maximum

print(maior_primo(17))
            