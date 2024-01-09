# Exercício 1 - Distância entre dois pontos
# Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, 
# respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem 
# corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.
# Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima
# longe
# na saída. Caso o contrário, quando a distância for menor que 10, imprima
# perto
# Dica: lembre-se que a fórmula da distância para dois pontos num plano cartesiano é a seguinte:
# d(x,y) = sqrt((x1-x2)² + (y1-y2)²)^{1/2}

x1 = float(input("Digite a primeira coordenada do  1o ponto: "))
x2 = float(input("Digite a segunda coordenada do 1o ponto: "))
x3 = float(input("Digite a primeira coordenada do 2o ponto: "))
x4 = float(input("Digite a segunda coordenada do 2o ponto: "))

dist = ((x1-x2)**2 + (x3-x4)**2)**(1/2)

if dist >= 10:
    print("longe")
else:
    print("perto")


