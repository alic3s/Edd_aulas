#Desenvolva um método (compara_pilha(pilha)) para a classe Pilha que verifique se uma pilha passada como parâmetro é igual a pilha que chama o método,
#retornando True ou False. Obs: Você deve deixar as pilhas do mesmo jeito que recebeu no início.

def compara(self, pilha2):
  if self.tamanho != pilha2.tamanho:
    return False
  else:
    no_atual1 = self.topo
    no_atual2 = pilha2.topo
    while(no_atual1 != None):
      if(no_atual1.dado != no_atual2.dado):
        return False
      no_atual1 = no_atual1.anterior
      no_atual2 = no_atual2.anterior
      return True
