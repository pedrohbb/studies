# Exercício 1: Fibonacci
# Implemente a função fibonacci(n), que recebe como parâmetro um número inteiro e devolve um número inteiro correspondente ao 
# n-ésimo elemento da sequência de Fibonacci. Sua solução deve ser implementada utilizando recursão.
# Exemplo:
# fibonacci(4)
# # deve devolver => 3
# fibonacci(2)
# # deve devolver => 1

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
