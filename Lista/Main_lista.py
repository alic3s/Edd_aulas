from Lista import Lista

lista = Lista()
print("Lista vazia:", lista)

lista.insereInicio(5)
print("Lista contém um único elemento:", lista)

nodo_anterior = lista.cabeca
lista.insereFim(nodo_anterior, 10)
print("Inserindo um novo elemento depois de um outro:", lista)
