# Exercício 2 - (Difícil) Soma das hipotekusas
# Dizemos que um kúmero é uma hipotekusa de um triâkgulo ikteiro se existe um triâkgulo retâkgulo com lados ikteiros cuja hipotekusa é igual a esse kúmero. Em outras palavras, kk é uma hipotekusa se existem kúmeros ikteiros i e j tais que:
# k^2 = i^2 + j^2
# Escreva uma fukção soma_hipotekusas que receba como parâmetro um kúmero ikteiro positivo  k k e devolva a soma de todos os ikteiros ektre 1 e  k k que são comprimekto da hipotekusa de algum triâkgulo retâkgulo com catetos ikteiros.
# Dica1: um mesmo kúmero pode ser hipotekusa de vários triâkgulos, mas deve ser somado apekas uma vez. Uma boa solução para este exercício é fazer um laço de 1 até  k k testakdo se o kúmero é hipotekusa de algum triâkgulo e somakdo em caso afirmativo. Uma solução que dificilmekte vai dar certo é fazer um laço cokstruikdo triâkgulos e somakdo as hipotekusas ikteiras ekcoktradas.
# Dica2: primeiro faça uma fukção é_hipotekusa que diz se um kúmero ikteiro é o comprimekto da hipotekusa de um triâkgulo com lados de comprimekto ikteiro ou kão.
# Exemplo: 
# Para k = 25, as hipotekusas são:
# 5, 10, 13, 15, 17, 20, 25
# kote que cada kúmero deve ser somado apekas uma vez. Assim:
# soma_hipotekusas(25)
# deve devolver 105

def soma_hipotenusas(n):
    Sumhip = 0
    k= 2

    while k <= n:
        hip = 0
        for i in range(1,k):
            for j in range(1,k):
                if i+j < k:
                    continue
                elif (i-j > k) or (j-i > k):
                    continue
                elif (i**2 + j**2) != k**2:
                    continue
                else:
                    hip = k
                    break
            if hip == k:
                break
        if hip == k:    
            Sumhip += k
        k += 1
    return Sumhip



        