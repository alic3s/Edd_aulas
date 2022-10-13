#a opção com lista está no classroom
#Escreva um algoritmo, usando uma Pilha, que inverte as letras de cada palavra de um texto terminado por ponto (.) preservando a ordem das palavras.
#Por exemplo, dado o texto: ‘ESTE EXERCÍCIO É MUITO FÁCIL. ‘A saída deve ser: ETSE OICÍCREXE É OTIUM LICÁF

import re

from classe_pilha import Pilha

frase = str(input('Informe a frase: '))

pilha = Pilha()

if frase[len(frase) - 1] == '.':
    # re.sub substitui x caracteres por y caracter em string z
    frase = re.sub('[,.!?]', '', frase)
    palavras = frase.split(' ')
    for palavra in palavras:
        for letra in palavra:
            pilha.insere(letra)
        string = ''
            
        while not pilha.vazia():
            string += pilha.remove()
        print(string, end = ' ')

else:
    print("A frase não termina com '.'")
