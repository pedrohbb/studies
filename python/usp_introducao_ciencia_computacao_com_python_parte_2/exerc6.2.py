# Exercício 2: Encontrando ímpares em uma lista
# Implemente a função encontra_impares(lista), que recebe como parâmetro uma lista de números inteiros e devolve uma outra 
# lista apenas com os números ímpares da lista dada.
# Sua solução deve ser implementada utilizando recursão.
# Dica: você vai precisar do método extend() que as listas possuem.

def encontra_impares(lista):
    new_list = []
    n = len(lista)
    if n == 0:
        return new_list
    else:
        if lista[0] % 2 == 1:
            new_list.append(lista[0])
            new_list.extend(encontra_impares(lista[1:]))
        else:
            new_list.extend(encontra_impares(lista[1:]))

        return new_list

