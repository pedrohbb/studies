# https://panda.ime.usp.br/aulasPython/static/aulasPython/aula08.html
# Exercício 8.5
# Nota: Exercício 5 da lista sobre repetições encaixadas.
# Sabe-se que cada número da forma n**3 é igual a soma de n ímpares consecutivos. Por exemplo,
# 1**3 = 1
# 2**3 = 3 + 5
# 3**3 = 7 + 9 + 11
# 4**3 = 13 + 15 + 17 + 19
# Dado um número inteiro m > 0, determinar os ímpares consecutivos cuja soma é igual a n**3, para n assumindo valores de 1 a m.

def cube_oddssum(n): #poderia melhorar, mas teria que usar matemática para isso
    k = 1

    while (k + k + 2*(n-1))*n/2 < n**3:
        k += 2

    if (k + k + 2*(n-1))*n/2 == n**3:
        return [(k + 2*i) for i in range(n)]
    
    else: 
        return "Não há solução"


def all_cube_oddssum_until(n):

    lst = []
    for i in range(1,n+1):
        lst.append(cube_oddssum(i))

    for i in range(len(lst)):

        a = ''
        for j in lst[i]:
            a += str(j) + ', '

        a = a[:-2]
        print(f"{i+1} é igual a soma dos números " + a)

    

def main():
    m = int(input("Insira um número inteiro positivo: "))

    all_cube_oddssum_until(m)


main()

