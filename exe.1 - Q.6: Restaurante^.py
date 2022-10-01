cont = total = 0

dicio = {1: ('Strogonoff', 15.00), 2: ('Feijoada', 14.00), 3: ('Lasanha', 16.00), 4: ('Arroz à grega', 6.00), 5: ('Frango à Parmegiana', 10.00)}

print('MENU'.center(25))

for k, v in dicio.items():
    f'({k}) {v[0]:^8} = R${v[1]:.2f}'

while True:
    valor = 0
    print(f'\n {cont+1}º')
    
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
            cont +=1
            break

        print()
        
    print(f'O total do {cont}º foi {valor:.2f}')

    total += valor

    flag_2 = (str(input('Encerrar o dia?(S/N): ')))

    if flag_2 != 'N':
        break
    
print(f'O total de {cont} pedidos é {total:.2f}')
