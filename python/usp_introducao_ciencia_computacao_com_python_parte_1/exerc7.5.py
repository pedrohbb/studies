# https://panda.ime.usp.br/aulasPython/static/aulasPython/aula08.html

# Exercício 8.1
# Nota: Questão 1 da Prova 1 de 2014.
# Na figura, no plano cartesiano, a região sombreada não inclui as linhas de bordo. Note que o eixo y cai bem no meio da figura, e usamos o lado do quadrado para indicar as ordenadas correspondentes.
# Escreva na página do desenho um programa que lê as coordenadas cartesianas (x, y) de um ponto, ambas do tipo float e imprime dentro se esse ponto está na região, e fora caso contrário.


x = float(input("Insira a primeira coordenada: "))
y = float(input("Insira a segunda coordenada: "))

def wherecoord(x,y):
    if x >= 5 or x <= -5 or y <= 0 or y >= 8:
        print("fora")
    elif x >= -3 and x <= 3 and y >= 1 and y <= 2:
            print("fora")
    else:
        Eyes = False
        for i in range(0,6,5):
            if (x >= (-4 + i)) and (x <= (-1 + i)) and y >= 4 and y <= 7:
                if (x >= (-3+i)) and (x <= (-2+i)) and y >= 5 and y <= 6:
                    print("dentro")
                else:
                    print("fora")

                Eyes = True
                break
            else:
                continue
        if Eyes == False:
            print("dentro")

wherecoord(x,y)

        