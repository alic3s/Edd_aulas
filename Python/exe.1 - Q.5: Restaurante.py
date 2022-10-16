valor = 0

dicio = {1: ('Strogonoff', 15.00), 2: ('Feijoada', 14.00), 3: ('Lasanha', 16.00), 4: ('Arroz à grega', 6.00), 5: ('Frango à Parmegiana', 10.00)}

print('MENU'.center(25))

for k, v in dicio.items():
    f'({k}) {v[0]:^8} = R${v[1]:.2f}'

while True:
    while True:
        opcao = int(input('Qual o seu pedido?:'))
        if 1<= opcao <= 5:
            break
        else:
            f'Opção inválida'
            
    print(f'Seu pedido foi: {dicio[opcao][0]}.')

    valor += dicio[opcao][1]

    flag = (str(input('Mais alguma coisa? (S/N): ')))

    if flag != 'S':
        break


print(f'O total dos pedidos foi {valor:.2f}')
