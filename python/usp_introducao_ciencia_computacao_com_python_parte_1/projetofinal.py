import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    S = 0
    for i in range(len(as_a)):
        S += abs(as_a[i] - as_b[i])/6
    
    return S


def calcula_assinatura(texto):
    count_words = 0
    total_lett = 0
    all_words = []
    count_caractsent = 0
    count_phr = 0
    count_caractphr = 0

    sents_list = separa_sentencas(texto)
    for sent in sents_list:

        phrs_list = separa_frases(sent)
        for phr in phrs_list:

            words_list = separa_palavras(phr)
            for word in words_list:
                total_lett += len(word)
                count_words += 1

            all_words += words_list
            count_caractphr += len(phr)
            
        count_caractsent += len(sent)
        count_phr += len(phrs_list)

    
    wal_ = total_lett / count_words
    ttr_ = n_palavras_diferentes(all_words) / count_words
    hlr_ = n_palavras_unicas(all_words) / count_words
    sal_ = count_caractsent / len(sents_list)
    sac_ = count_phr / len(sents_list)
    pal_ = count_caractphr / count_phr

    signat = [wal_, ttr_, hlr_, sal_, sac_, pal_]

    return signat
    
def avalia_textos(textos, ass_cp=0):
    
    a = []
    for texto in textos:
        sign = calcula_assinatura(texto)
        a.append(compara_assinatura(sign,ass_cp))
    
    ind = a.index(min(a)) + 1
    
    return ind
            