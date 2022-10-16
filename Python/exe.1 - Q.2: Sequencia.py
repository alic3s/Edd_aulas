listinha = list()

print('Caso queira parar, digite 0')
while True:
    numeros = int(input('Digite um valor: '))
    if numeros == 0:
        break
    else:
        listinha.append(numeros)
print()

maior = max(listinha)
print(f'O maior elemento dessa sequência foi: {maior}')

print()
print(listinha)
