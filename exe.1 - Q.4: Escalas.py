temp1 = float(input('Informe o valor da 1º temperatura: '))
temp_1 = str(input('Informe se a escala da 1º temperatura é C ou F: '))

tuplinha = (temp1, temp_1)

temp2 = float(input('Informe o valor da 2º temperatura: '))
temp_2 = str(input('Informe se a escala da 2º temperatura é C ou F: '))

tuplinha_2 = (temp2, temp_2)

def maior(tuplinha, tuplinha_2):
     if tuplinha[1] != tuplinha_2[1]:
        if tuplinha_2 == 'F':
            far = (tuplinha[0] * 1.8) + 32
            
        elif tuplinha_2 == 'C':
            cel = (tuplinha[0] - 32) / 1.8
     return far


maior(tuplinha, tuplinha_2)
