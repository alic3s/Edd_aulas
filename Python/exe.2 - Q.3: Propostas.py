#Um edital de concorrência pública avaliará 5 propostas considerando
#três critérios: qualidade, preço e prazo. Cada um dos três recebe uma nota de zero
#a dez. Escreva um programa que leia as notas de preço, prazo e qualidade de cada
#proposta e escreva a nota geral de cada proposta bem como qual das propostas
#apresentadas ganhou a concorrência (obteve maior nota). Para calcular as notas
#deve-se utilizar os seguintes critérios: 1. Se a nota da qualidade for inferior a 7, a
#nota geral será 0, independente dos outros fatores. 2- Se a qualidade for igual ou
#superior a 7, e a nota do preço for igual ou superior a 7, então a nota será a média
#das três notas. 3- Se a nota da qualidade for igual ou superior a 7 e a do preço for
#inferior a 7, então a nota geral será será (qualidade+2*preço+prazo)/4.


p1 = {1: 'Preço', 2: 'Prazo', 3: 'Qualidade'}
p2 = {1: 'Preço', 2: 'Prazo', 3: 'Qualidade'}


p1[1] = (int(input('Informe a nota do preço: ')))
p1[2] = (int(input('Informe a nota do prazo: ')))
p1[3] = (int(input('Informe a nota da qualidade: ')))


p2[1] = (int(input('\nInforme a nota do preço: ')))
p2[2] = (int(input('Informe a nota do prazo: ')))
p2[3] = (int(input('Informe a nota da qualidade: ')))

nota_geral1 = p1[1] + p1[2] + p1[3]
nota_geral2 = p2[1] + p2[2] + p2[3]

print(f'A nota geral (sem critérios) da proposta foi:{nota_geral1}')
print(f'A nota geral (sem critérios) da proposta foi: {nota_geral2}')


if p1[3] < 7:
    nota_geral1 = 0
elif p1[3] >= 7 and p1[1] >= 7:
    nota_geral1 = nota_geral1 / 3
elif p1[3] >= 7 and p1[1] < 7:
    nota_geral1 = (p1[3] + p1[1] + p1[2]) / 4

print(nota_geral1)
    
if p1[1] + p1[2] + p1[3] > p2[1] + p2[2] + p2[3]:
    print(f'A proposta com maior nota foi a primeira: {p1}')
else:
    print(f'A proposta com maior nota foi a segunda: {p2}')
