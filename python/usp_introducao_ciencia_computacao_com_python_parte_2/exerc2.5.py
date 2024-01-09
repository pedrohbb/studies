# # https://panda.ime.usp.br/aulasPython/static/aulasPython/aula16.html

# Exercício 16.1
# Parte A

# Escreva uma função com protótipo

# def insereSeNovo (nome, lista):
#     ''' (str, list) -> int
#         modifica a lista, inserindo nome na lista.
#         Retorna a posição de nome na lista ou None caso ele já exista.
#     '''
# que devolve a posição em que o string x ocorre em lista ou, caso x não estiver na lista, insere x no final da lista e devolve o índice dessa posição.

# # escreva a sua função abaixo e remova o print()
# def insereSeNovo (nome, lista):
#     print("Vixe! Ainda nao fiz essa funcao!")

# # Codigo para testar a sua funcao
# lista = ["Ronaldo", "Romario", "Rivelino"]
# pos = insereSeNovo("Romario", lista)
# pos = insereSeNovo("Pele", lista)
# pos = insereSeNovo("Rivelino", lista)
# print(lista, " que deve ser Ronaldo, Romario, Rivelino, Pele")

# Parte B

# Escreva um programa que leia uma sequência de nomes e, usando a função do item anterior, conte quantas vezes cada nome ocorre na sequência.

# Exemplo:

# Para n = 7 e a sequência Neimar Messi Kaka Neimar Neimar Messi Zico

# a saída deve ser:

# Neimar ocorre 3 vezes
# Messi ocorre 2 vezes
# Kaka ocorre 1 vezes
# Zico ocorre 1 vezes

# # escreva o seu programa abaixo e remova o print()
# print("Vixe! Ainda nao fiz esse exercicio!")

def insereSeNovo(nome, lst):
    ''' (str, list) -> int
        modifica a lista, inserindo nome na lista.
        Retorna a posição de nome na lista ou None caso ele já exista.
    '''
    if nome in lst:
        return lst.index(nome)
    else:
        lst.append(nome)
        return len(lst)-1

def contaNome(lista):
    #seria mais simples ao usar set, mas como ainda não foi dado no curso, vou fingir que não tive essa ideia
    
    count_nomes = []
    dif_nomes = []
    for nome in lista:
        
        aux = len(lista)
        idx = insereSeNovo(nome,lista)
        if aux == len(lista):
            if nome not in dif_nomes:
                dif_nomes.append(nome)
                count_nomes.append(1)
            else:
                count_nomes[dif_nomes.index(nome)] += 1
        else:
            del lista[idx]
            continue
    
    for i in range(len(count_nomes)):
        print(f'{dif_nomes[i]} ocorre {count_nomes[i]} vezes')

lst = 'Neimar Messi Kaka Neimar Neimar Messi Zico'.split()
contaNome(lst)
