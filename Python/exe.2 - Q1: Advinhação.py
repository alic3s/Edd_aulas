from random import randint

print('\nSeja bem-vindo ao jogo da adivinhação!\n')

tentativas = 3
n = randint(1, 11)

flag = 'Ss'

while True:
    teste = (int(input('Digite um número inteiro até 10: ')))

    if n != teste:
        tentativas-=1
        print(f'Ops..., agora você tem {tentativas} tentativa(s).\n')

        if n < teste:
            print(f'O número é menor que {teste}.\n')
        
        if n > teste:
            print(f'O número é maior que {teste}.')

    else:
        print('\nVocê acertou!')

        flag = (str(input('\nDeseja tentar novamente?(S/N): ')))

    if tentativas == 0:
        print(f'Você perdeu! Seu número de tentativas atuais é {tentativas}')
    
        flag = (str(input('\nDeseja tentar novamente?(S/N): ')))

    if flag in 'Nn':
        break

print('\nJogo finalizado. Até mais!\n')
