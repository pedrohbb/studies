# Exercício 2: Fatorial
# Implemente a função fatorial(x), que recebe como parâmetro um número inteiro e devolve um número inteiro correspondente ao 
# fatorial de x.
# Sua solução deve ser implementada utilizando recursão.

def fatorial(x):
    if x == 0 or x == 1:
        return 1
    if x > 1:
        return x*fatorial(x-1)