# primeira opção
import re

def inverte(palavra):
    if re.match(r'^\w+$',palavra):
        return palavra[::-1]
    return palavra

frase = (str(input('Digite uma frase: ')))

invertida = ''.join(inverte(palavra) for palavra in re.split(r'(\w+)',frase))
print(invertida)


frase = input('Digite uma frase: ')
print('Você digitou: {}'.format(frase))
invertida = ' '.join(palavra[::-1] for palavra in frase.split())
print('A frase que você digitou invertida fica: {}'.format(invertida))

#segunda opção
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
   
#terceira opção está no classroom
