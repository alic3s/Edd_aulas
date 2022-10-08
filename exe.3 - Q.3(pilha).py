#a opção com lista está no classroom

import re

frase = input('Informe a frase: ')
pilha = Pilha()

if frase[len(frase) - 1] == '.':
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
    print('A frase não termina com .')
