import random

s1 = [random.randrange(10, 41, 1) for i in range(7)]
s2 = [random.randrange(10, 41, 1) for i in range(7)]
s3 = [random.randrange(10, 41, 1) for i in range(7)]
s4 = [random.randrange(10, 41, 1) for i in range(7)]

print('\n', s1,'\n', s2, '\n', s3, '\n', s4)
print()

mes = s1 + s2 + s3 + s4

media = sum(mes) / len(mes)

media_ac = [0, 0, 0, 0]

menor = min(mes)
maior = max(mes)

print(f'A média do mês é {round(media,2)}')

temp = mes.index(maior)
sem_m = list()

for t in s1:
    if t > media:
        media_ac[0] += 1

for t in s2:
    if t > media:
        media_ac[1] += 1

for t in s3:
    if t > media:
        media_ac[2] += 1

for t in s4:
    if t > media:
        media_ac[3] += 1

print()

for cont in range(0,4):
    if media_ac[cont] > 3:
        print(f'A {cont+1}º semana teve {media_ac[cont]} temperaturas acima da média do mês')
        
print()

print(f'A menor temperatura foi {menor}°C e a maior temperatura foi {maior}°C')

print()

if 0 <= temp < 7:
    sem_m = s1[:]

if 7 <= temp < 14:
    sem_m = s2[:]
    
if 14 <= temp < 21:
    sem_m = s3[:]
    
if 21 <= temp < 28:
    sem_m = s4[:]
    
print(sem_m)
print()

dias = ['D', 'S', 'T', 'Q', 'Q', 'S', 'S']

for cont in range(0,7):
    print(f'{dias[cont]}: ', '■' * sem_m[cont])
