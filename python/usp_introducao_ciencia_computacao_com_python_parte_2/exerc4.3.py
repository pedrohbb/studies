# Exercício 1: Gerando listas grandes
# Escreva a função lista_grande(n), que recebe como parâmetro um número inteiro n e devolve uma lista contendo n números inteiros aleatórios.

import random

def lista_grande(n: int) -> list:
    count = 0
    lista = []
    if n == 0:
        return lista
    while True:
        numb = random.randint(-10**(count+1),10**(count+1))
        if numb in lista:
            continue
        lista.append(numb)
        count += 1
        if count == n:
            break
    return lista