# Exercício 2: Soma de matrizes
# Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz que represente sua soma caso as matrizes tenham dimensões iguais. Caso contrário, a função deve devolver False.

# Exemplos:
# m1 = [[1, 2, 3], [4, 5, 6]]
# m2 = [[2, 3, 4], [5, 6, 7]]
# soma_matrizes(m1, m2) => [[3, 5, 7], [9, 11, 13]]

# m1 = [[1], [2], [3]]
# m2 = [[2, 3, 4], [5, 6, 7]]
# soma_matrizes(m1, m2) => False
def dimensoes(matriz: list):
    i = len(matriz)
    if type(matriz[0]) in {float,int}:
        j = i
        i = 1
        print(f"{i}x{j}")
    else:
        j = len(matriz[0])
        for k in range(len(matriz)):
            notmatriz = False
            if len(matriz[k]) != j:
                print("Objeto inserido não é matriz")
                notmatriz = True
                break
        if not notmatriz:
            return (i,j)

def soma_matrizes(m1,m2):
    if dimensoes(m1) == dimensoes(m2):
        m3 = []
        for i in range(len(m1)):
            aux = []
            for j in range(len(m1[0])):
                aux.append(m1[i][j] + m2[i][j])
            m3.append(aux)
        return m3
    else:
        return False

print(soma_matrizes([[1,2,3],[4,5,6]], [[1,0,0],[0,1,0]]))