# Exercício 1 - Primos
# Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).
# Exemplo:
# >>>n_primos(2)
# 1
# >>>n_primos(4)
# 2
# >>>n_primos(121)
# 30

def n_primos(x):
    Primos = ''
    for i in range(2,x+1):
        Prim = True
        for j in range (2,i):
            if i % j == 0:
                Prim = False
                break
        if Prim == True:
            Primos += 'i'
    return len(Primos)
