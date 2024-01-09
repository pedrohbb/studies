# Exercício 2: Matrizes multiplicáveis
# Duas matrizes são multiplicáveis se o número de colunas da primeira é igual ao número de linhas da segunda. Escreva a função sao_multiplicaveis(m1, m2) que recebe duas matrizes como parâmetro e devolve True se as matrizes forem multiplicavéis (na ordem dada) e False caso contrário.

# Exemplos:

# m1 = [[1, 2, 3], [4, 5, 6]]
# m2 = [[2, 3, 4], [5, 6, 7]]
# sao_multiplicaveis(m1, m2) => False

# m1 = [[1], [2], [3]]
# m2 = [[1, 2, 3]]
# sao_multiplicaveis(m1, m2) => True

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

def sao_multiplicaveis(m1, m2):
    m1_lin, m1_col = dimensoes(m1)
    m2_lin, m2_col = dimensoes(m2)
    if m1_col == m2_lin:
        return True
    else:
        return False
