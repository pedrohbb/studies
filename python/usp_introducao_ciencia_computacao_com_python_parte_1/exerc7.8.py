# https://panda.ime.usp.br/aulasPython/static/aulasPython/aula08.html
# Exercício 8.4
# Dados um número inteiro n > 0, e uma sequência com n números inteiros, verificar se a sequência é uma progressão aritmética.

def pafinder(lst):
    ratio = []
    
    for i in range(1,len(lst)):
        r = int(lst[i]) - int(lst[i-1])
        if r not in ratio:
            ratio.append(r)

    if len(ratio) > 1:
        print("não é uma P.A.")
    else:
        print("é uma P.A.")

def main():
    seq = input("Insira os números em sequência (ex.: 1,2,3,4): ").split(',')
    
    for i in range(len(seq)):

        while (' ' in seq[i]): 
            x = seq[i].index(' ')

            if x == len(seq[i])-1:
                seq[i] = seq[i][:-1]
            else:
                seq[i] = seq[i][:x] + seq[i][x+1:]
           
    algs = '0123456789'
    InvChar = False
    for member in seq:
        for number in member:
            if number not in algs:
                InvChar = True
                break
    if InvChar == True:
        print("Formato inválido")
    else:
        pafinder(seq)
        
main()