def maior(tupla1, tupla2):
    if tupla1[1] == tupla2[1]:
        if tupla2[1] == 'F':
            if tupla2[0] > tupla1[0]:
                print(f'{tupla2[0]}°F é maior que {tupla1[0]}°F')
            
            elif tupla1[0] > tupla2[0]:
                print(f'{tupla1[0]}°F é maior que {tupla2[0]}°F')

        elif tupla2[1] == 'C':
            if tupla2[0] > tupla1[0]:
                print(f'{tupla2[0]}°C é maior que {tupla1[0]}°C')
            
            elif tupla1[0] > tupla2[0]:
                print(f'{tupla1[0]}°C é maior que {tupla2[0]}°C')
    
    
    if tupla1[1] != tupla2[1]:
         if tupla2[1] == 'F':
            far = (tupla1[0] * 1.8) + 32
            if far > tupla2[0]:
                print(f'{far:.1f}°F é maior que {tupla2[0]}°F')
            elif tupla2[0] > far:
                print(f'{tupla2[0]}°F é maior que {far:.1f}°F')

         elif tupla2[1] == 'C':
            cel = (tupla1[0] - 32) / 1.8
            if cel > tupla2[0]:
                print(f'{cel:.1f}°C é maior que {tupla2[0]}°C')
            elif tupla2[0] > cel:
                print(f'{tupla2[0]}°C é maior que {cel:.1f}°C')




temp1 = float(input('Qual o valor da 1º temperatura?: '))
print()
esc1 = str(input('Qual a escala da 1º temperatura?(C ou F): '))
print()
tupla1 = (temp1, esc1)

temp = float(input('Qual o valor da 2º temperatura?: '))
print()
esc = str(input('Qual a escala da 2º temperatura?(C ou F): '))
print()
tupla2 = (temp, esc)

print(maior())
print()
