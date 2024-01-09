# Exercício 2
# Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.
# Por exemplo:
# digite a largura: 10
# digite a altura: 3
# ##########
# #        #
# ##########
# digite a largura: 2
# digite a altura: 2
# ##
# ##

m = int(input("digite a largura: "))
n = int(input("digite a altura: "))

for i in range(1,n+1):
    if i == 1 or i == n:
        print('#'*m)
    else:
        print('#' + ' '*(m-2) + '#')

    
