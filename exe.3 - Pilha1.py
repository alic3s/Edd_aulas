#Verificação de expressão aritmética

def verificar(self, entrada):
    pilha = Pilha()
    for s in entrada:
        if s == '(' or s == '[' or s == '{':
            pilha.insere(s)
        elif s == ')' or s == ']' or s == '}':
            if (pilha.vazia()):
                return False
            if s == ')' and pilha.remove != '(':
                return False
            if s == ']' and pilha.remove != '[':
                return False
            if s == '}' and pilha.remove != '{':
                return False
    if pilha.vazia():
        return True
    else:
        return False

#as expressoes sao: [(x + y) * 2] = 0; [(x + y] * 2) = 0; [(x + y * 2) = 0

string = (list(input('Digite a expresão: ')))
