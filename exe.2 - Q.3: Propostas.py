p1 = {1: 'Preço', 2: 'Prazo', 3: 'Qualidade'}
p2 = {1: 'Preço', 2: 'Prazo', 3: 'Qualidade'}
p3 = {1: 'Preço', 2: 'Prazo', 3: 'Qualidade'}
p4 = {1: 'Preço', 2: 'Prazo', 3: 'Qualidade'}
p5 = {1: 'Preço', 2: 'Prazo', 3: 'Qualidade'}

p1[1] = (int(input('Informe a nota do preço: ')))
p1[2] = (int(input('Informe a nota do prazo: ')))
p1[3] = (int(input('Informe a nota da qualidade: ')))

p2[1] = (int(input('Informe a nota do preço: ')))
p2[2] = (int(input('Informe a nota do prazo: ')))
p2[3] = (int(input('Informe a nota da qualidade: ')))

p3[1] = (int(input('Informe a nota do preço: ')))
p3[2] = (int(input('Informe a nota do prazo: ')))
p3[3] = (int(input('Informe a nota da qualidade: ')))

p4[1] = (int(input('Informe a nota do preço: ')))
p4[2] = (int(input('Informe a nota do prazo: ')))
p4[3] = (int(input('Informe a nota da qualidade: ')))

p5[1] = (int(input('Informe a nota do preço: ')))
p5[2] = (int(input('Informe a nota do prazo: ')))
p5[3] = (int(input('Informe a nota da qualidade: ')))

print('A nota geral da proposta foi: ', p1[1] + p1[2] + p1[3])
print('A nota geral da proposta foi: ', p2[1] + p2[2] + p2[3])
print('A nota geral da proposta foi: ', p3[1] + p3[2] + p3[3])
print('A nota geral da proposta foi: ', p4[1] + p4[2] + p4[3])
print('A nota geral da proposta foi: ', p5[1] + p5[2] + p5[3])

max_key1 = max(p1, key = p1.get)
print(max_key)

max_key2 = max(p2, key = p2.get)
print(max_key2)

max_key3 = max(p3, key = p3.get)
print(max_key3)

max_key4 = max(p4, key = p4.get)
print(max_key4)

max_key5 = max(p5, key = p5.get)
print(max_key5)
