peso = 0
elevador = 0

while True:
    p = (float(input(f'Informe o peso da {elevador + 1}ª pessoa em kg: ')))

    if peso + p <= 800:
        peso += p
        elevador += 1
    else:
        print(f'A carga total suportada foi excedida! O peso contido dentro do elevador agora é de {peso}')
        print(f'Nesse momento há {elevador} pessoa(s) dentro do elevador')
        break
