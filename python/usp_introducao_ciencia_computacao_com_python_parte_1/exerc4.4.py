# Exercício 1
# Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".
# Exemplos:
# Digite um número inteiro: 13
# primo
# Digite um número inteiro: 12
# não primo

n = int(input("Insira um número: "))

i=2
while i <= int(n**(1/2)):
    if n % i == 0:
        print("não primo")
        break
    else:
        if i == int(n**(1/2)):
            break
        else:
            i=i+1

if i == int(n**(1/2)):
     print("primo")
    
