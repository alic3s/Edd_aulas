#3 filas independentes do tamanho seguindo a ordem 1,2,3. O identificador da fila e o elemento(dado); pode usar tupla
'''Crie um PROGRAMA que simule a multiplexação de três fluxos contínuos de
dados que vão utilizar um único canal (por exemplo, três programas que querem utilizar a
placa de rede do computador). Considere que o algoritmo de prioridade de uso do canal é
FIFO. Considere ainda que quando os fluxos estão enviando dados continuamente, são
enfileirados no canal, o primeiro a chegar de cada fluxo, alternando entre os fluxos. Os
fluxos podem não ter o mesmo numero de elementos enfileirado Para efetuar a simulação,
seu programa deverá passar pelos seguintes passos:
1. Programa lê do teclado diversos números inteiros que são enfileirados em uma fila de
inteiros que representa o primeiro fluxo de dados.
2. Programa lê do teclado diversos números inteiros que são enfileirados em uma outra fila
de inteiros que representa o segundo fluxo de dados.
3. Programa lê do teclado diversos números inteiros que são enfileirados em uma outra fila
de inteiros que representa o terceiro fluxo de dados.
4. Programa imprime na tela os elementos das três filas para que possamos visualizar o
estado dos fluxos.
5. Programa cria uma outra fila (que representará o canal compartilhado).
Essa fila, porém, não será apenas uma fila de inteiros, mas uma fila de objetos que
armazenam dois inteiros (um para armazenar o valor que vem dos fluxos e outro
para armazenar o identificador do fluxo).
6. Programa alterna entre os fluxos desenfileirando um a um os valores.
A cada iteração, o programa deve desenfileirar um valor de um dos fluxos e enfileirar
esse valor e o identificador do fluxo na fila do canal.
Na iteração seguinte, deverá fazer o mesmo com outro fluxo. E assim será até que
todos os fluxos estejam vazios.
• A medida em que um fluxo se esgota, não haverá mais desenfileiramento nele.
7. Ao final, deverá ser impresso na tela os elementos da fila do canal (identificador e valor).'''

from classe_fila import Fila

fluxo1 = Fila()
fluxo2 = Fila()
fluxo3 = Fila()
fluxo4 = Fila()

print('#' * 40 + '\n' + 'Multiplexação'.center(40) + '\n' + '#' * 40)

n = 0
while True:
    f1 = int(input(f'\nDigite o {n+1}º elemento inteiro do 1º fluxo: '))

    fluxo1.insere((f1, 1))
    
    n += 1

    flag = str(input('\nDeseja continuar preenchedo o fluxo 1? (S ou N): '))

    if flag == 'S':
        continue
    elif flag == 'N':
        break

i = 0
while True:
    f2 = int(input(f'\nDigite o {i+1} elemento inteiro do 2º fluxo: '))

    fluxo2.insere((f2, 2))

    i += 1

    flag = str(input('\nDeseja continuar preenchendo o fluxo 2? (S ou N): '))

    if flag == 'S':
        continue
    elif flag == 'N':
        break

v = 0 
while True:
    f3 = int(input(f'\nDigite o {v+1} elemento inteiro do 3º fluxo: '))

    fluxo3.insere((f3, 3))

    v += 1

    flag = str(input('\nDeseja continuar preenchendo o fluxo 3? (S ou N): '))

    if flag == 'S':
        continue
    elif flag == 'N':
        break

print()

print(f'\nFluxo 1: {fluxo1}, \nFluxo 2: {fluxo2}, \nFluxo 3: {fluxo3}')

canal = fluxo1.tamanho + fluxo2.tamanho + fluxo3.tamanho

for i in range(canal):
    if not fluxo1.vazia():
        fluxo4.insere(fluxo1.remove())
    if not fluxo2.vazia():
        fluxo4.insere(fluxo2.remove())
    if not fluxo3.vazia():
        fluxo4.insere(fluxo3.remove())
print()

print(f'A fila do canal é {fluxo4}')
