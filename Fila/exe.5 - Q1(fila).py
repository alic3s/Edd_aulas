def compare(self, F2):
        if self.tamanho != F2.tamanho:
            return False
        else:
            atual1 = self.cabeca
            atual2 = F2.cabeca
            while atual1 != None:
                if atual1.dado != atual2.dado:
                    return False
                atual1 = atual1.proximo
                atual2 = atual2.proximo
            return True

F1 = Fila()

F1.insere(1)
F1.insere(2)
F1.insere(3)
F1.insere(4)

print(F1)

F2 = Fila()

F2.insere(1)
F2.insere(2)
F2.insere(3)

print(F1.compare(F2))
