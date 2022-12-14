from Lista import Lista

#inserir elementos no início da lista
lista = Lista()
print("Lista vazia:", lista)

lista.insereInicio(10)
print("Lista contém um único elemento:", lista)

lista.insereInicio(20)
print("Inserindo um novo elemento:", lista)

#inserir elementos no fim da lista
lista = Lista()
print("Lista vazia:", lista)

lista.insereInicio(5)
print("Lista contém um único elemento:", lista)

nodo_anterior = lista.cabeca
lista.insereFim(nodo_anterior, 10)
print("Inserindo um novo elemento depois de um outro:", lista)

lista = Lista()
for i in range(6):
    lista.insereInicio(i)
print("Lista:", lista)

for i in range(6, -3, -2):
    elemento = lista.busca(i)
    if elemento:
        print("Elemento {0} presente na lista!".format(i))
    else:
        print("Elemento {0} não encontrado.".format(i))
