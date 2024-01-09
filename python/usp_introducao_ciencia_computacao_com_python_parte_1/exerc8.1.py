# Exercício 1 - Removendo elementos repetidos
# Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.
# Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?
# Exemplo: 
# >>>lista = [2, 4, 2, 2, 3, 3, 1]
# >>>remove_repetidos(lista)
# [1, 2, 3, 4]
# >>>remove_repetidos([1, 2, 3, 3, 3, 4])
# [1, 2, 3, 4]

def remove_repetidos(lst):
    for number in lst:

        while number in lst:        
            ind = lst.index(number)
            lst.remove(number)

            if number not in lst:
                lst.insert(ind,number)
                break

    return sorted(lst, reverse = False)

#O primeiro altera a lista original e o segundo retorna um novo objeto criado a partir do primeiro
