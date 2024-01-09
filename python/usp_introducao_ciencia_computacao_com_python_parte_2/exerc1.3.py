# Exercício 1: Imprimindo matrizes
# Como proposto na primeira vídeo-aula da semana, escreva uma função imprime_matriz(matriz), que recebe uma matriz como parâmetro e imprime a matriz, linha por linha. Note que NÃO se deve imprimir espaços após o último elemento de cada linha!

# Dica: lembre da primeira parte do curso, na semana 7! A função "print" em geral adiciona uma quebra de linha ao final, mas você pode controlar isso usando o argumento opcional "end"dessa forma:

# >>>print("oi")
# oi
# >>>
# >>>print("oi", end="")
# oi>>>

# Exemplos:

# minha_matriz = [[1], [2], [3]]
# imprime_matriz(minha_matriz)
# 1
# 2
# 3

# minha_matriz = [[1, 2, 3], [4, 5, 6]]
# imprime_matriz(minha_matriz)
# 1 2 3
# 4 5 6

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

def imprime_matriz(matriz):
    lin, col = dimensoes(matriz)
    
    for i in range(lin):
        for j in range(col):
            if j != col-1:
                print(matriz[i][j], end= ' ')
            else:
                print(matriz[i][j], end= '')
        print('')

imprime_matriz([[1,2,3],[4,5,6],[7,8,9]])


