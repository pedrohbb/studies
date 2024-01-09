# Exercício 1: Tamanho da matriz
# Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e imprime as dimensões da matriz recebida, no formato iXj.

# Exemplos:
# minha_matriz = [[1], [2], [3]]
# dimensoes(minha_matriz)
# 3X1

# minha_matriz = [[1, 2, 3], [4, 5, 6]]
# dimensoes(minha_matriz)
# 2X3

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
            print(f"{i}x{j}")