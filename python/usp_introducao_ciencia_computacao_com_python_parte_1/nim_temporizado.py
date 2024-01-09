import time

def computador_escolhe_jogada(n,m):
    for i in range(1,m+1):
        x = i
        if ((n-x) % (m+1)) == 0:
            break
        else:
            continue
    return x

def usuario_escolhe_jogada(n,m): 
    while True:
        try:
            y = float(input("Sua jogada: "))
            
            if int(y) != y:
                print("Oops! Jogada inválida! Tente de novo.")
                continue
            elif y > m:
                print(f"Oops! Jogada inválida! Tente de novo.")
                continue
            elif y <= 0:
                print("Oops! Jogada inválida! Tente de novo.")
            else:
                y = int(y)
                break
                
        except:
            print("Oops! Jogada inválida! Tente de novo.")
            continue
    return y

def partida():
    while True:
        n = int(input("Quantas peças? "))
        time.sleep(1)
        m = int(input("Limite de peças por jogada? "))
        time.sleep(1)
        if n < m:
            print("Erro! Limite de peças por jogada não deve ser superior ao total")
        else:
            break

    if (n % (m+1)) != 0:
        time.sleep(1)
        print("\nComputador começa!\n")
        a = computador_escolhe_jogada(n,m)
        rest = n - a
        time.sleep(1)
        print(f"O Computador retirou {a} peças.")
        time.sleep(1)
        print(f"Agora restam apenas {rest}.\n")
        count = 1      
    else:
        time.sleep(1)
        print("\nVocê começa!\n")
        b = usuario_escolhe_jogada(n,m)
        time.sleep(1)
        print(f"Você retirou {b} peças.")      
        rest = n - b
        time.sleep(1)
        print(f"Agora restam apenas {rest}.")
        count = 0
        
    if count == 1 and rest > 0:
        while True:
            time.sleep(1)
            b = usuario_escolhe_jogada(rest,m)
            rest = rest - b
            print(f"Você retirou {b} peças.")
            time.sleep(1)
            print(f"Agora restam apenas {rest}.\n")
            time.sleep(1)
            a = computador_escolhe_jogada(rest,m)
            rest = rest - a

            if rest == 0:
                time.sleep(1)
                print(f"O Computador retirou {a} peças.")
                time.sleep(1)
                print("\nFim do jogo! O Computador ganhou!")
                break
            else:
                time.sleep(1)
                print(f"O Computador retirou {a} peças.")  
                time.sleep(1)
                print(f"Agora restam apenas {rest}.\n")
    elif count == 1 and rest == 0:
        time.sleep(1)
        print("\nFim do jogo! O Computador ganhou!")      
    else:
        while True:

            a = computador_escolhe_jogada(rest,m)
            rest = rest - a
            if rest == 0:
                time.sleep(1)
                print(f"\nO Computador retirou {a} peças.")
                time.sleep(1)
                print("\nFim do jogo! O Computador ganhou!")
                break
            else:
                time.sleep(1)
                print(f"\nO Computador retirou {a} peças.")   
                time.sleep(1)
                print(f"Agora restam apenas {rest}.\n") 
                b = usuario_escolhe_jogada(rest, m)
                rest = rest - b
                time.sleep(1)
                print(f"Você retirou {b} peças agora restam apenas {rest}")
            
def campeonato():
    for i in range(1,4):
        time.sleep(1)
        print(f"\nA {i}ª partida está prestes a começar! \n")
        partida()
    print("Placar: Você 0 X 3 Computador")


while True:
    try:
        x = int(input("Insira '1' para partida única ou '0' para melhor de três: "))
        if x==1:      
            partida()     
        elif x==0:
            campeonato()
        
        else: 
            print("Entrada inválida!")

        break
    except:
        print("Entrada inválida!")