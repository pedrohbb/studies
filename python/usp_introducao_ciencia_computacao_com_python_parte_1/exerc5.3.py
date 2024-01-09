# Exercício 3 - Vogais
# Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.
# Exemplos de execução no shell de Python
# >>> vogal("a")
# True
# >>> vogal("b")
# False
# >>> vogal("E")
# True
# Os valores True e False devolvidos devem ser do tipo bool (booleanos), e não strings

def vogal(a):
    A = "aeiouAEIOU"
    if len(a) == 1:
        if a in A:
            return True
        else:
            return False
            
print(vogal('a'))
