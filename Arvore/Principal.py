class Nodo:
    def __init__(self, dado=None):
        self.dado = dado
        self.dir = None
        self.esq = None
    
    def __str__(self):
        return str(self.dado)
    

class Arvore:
    def __init__(self):
        self.raiz = None


    def inserir(self, dado):
        if self.raiz is None:
            novo_nodo = Nodo(dado)
            self.raiz = novo_nodo
        
        elif dado < self.raiz.dado:
            if self.raiz.esq is None:
                novo_nodo = Nodo(dado)
                self.raiz.esq = novo_nodo

            else:
                subarvore = Arvore()
                subarvore.raiz = self.raiz.esq
                subarvore.inserir(dado)

        else:
            if self.raiz.dir is None:
                novo_nodo = Nodo(dado)
                self.raiz.dir = novo_nodo
            
            else:
                subarvore = Arvore()
                subarvore.raiz = self.raiz.dir
                subarvore.inserir(dado)
    

    def busca(self, elemento):
        if self.raiz is None:
            return False
        
        if self.raiz.dado == elemento:
            return True
        
        if elemento < self.raiz.dado:
            subarvore = Arvore()
            subarvore.raiz = self.raiz.esq
            return subarvore.busca(elemento)
        
        else:
            subarvore = Arvore()
            subarvore.raiz = self.raiz.dir
            return subarvore.busca(elemento)
    

    def imprimir(self):
        if (self.raiz != None):
            subE = Arvore()
            subE.raiz = self.raiz.esq
            subE.imprimir()
            print(self.raiz, end = '')

            subD = Arvore()
            subD.raiz = self.raiz.dir
            subD.imprimir()
    
    #questão 1 e 2 pedi a alguém ou ver se tirei foto

    def contagem(self):
        if (self.raiz==None):
            return 0
        
        else:
            subE=Arvore()
            subE.raiz=self.raiz.esq
            subD=Arvore()
            subD.raiz=self.raiz.dir
            return (subE.contagem() + 1 + subD.contagem())
    

    def remover(self, elemento, nodo=None):
        if nodo==None:
            nodo=self.raiz
            if nodo==None:
                return nodo

        if elemento<nodo.dado:
            subE=Arvore()
            subE.raiz=nodo.esq
            nodo.esq=subE.remover(elemento)

        elif elemento>nodo.dado:
            subD=Arvore()
            subD.raiz=nodo.dir
            nodo.dir=subD.remover(elemento)
        
        else:
            if nodo.esq is None:
                return nodo.dir
            if nodo.dir is None:
                return nodo.esq
            else:
                subD=Arvore()
                subD.raiz=nodo.dir
                substituto=subD.menor()
                nodo.dado=substituto
                nodo.dir=self.remover(substituto, nodo.dir)
                return nodo
