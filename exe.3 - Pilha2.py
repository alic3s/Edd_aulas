import re

def inverte(palavra):
    if re.match(r'^\w+$',palavra):
        return palavra[::-1]
    return palavra

frase = input('Ai se eu te pego.')

invertida = ''.join(inverte(palavra) for palavra in re.split(r'(\w+)',frase))
print(invertida)



frase = input('Digite uma frase: ')
print('Você digitou: {}'.format(frase))
invertida = ' '.join(palavra[::-1] for palavra in frase.split())
print('A frase que você digitou invertida fica: {}'.format(invertida))
