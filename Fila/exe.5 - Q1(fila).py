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
