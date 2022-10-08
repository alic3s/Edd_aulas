#Verificação de expressão aritmética

def verifica(entrada):
    pilha_s = Pilha()
    for s in entrada:
        if s == '(' or s == '[' or s == '{':
            pilha_s.insere(s)
        elif s == ')' or s == ']' or s == '}':
            if (pilha_s.vazia()):
                return False
            if s == ')' and pilha_s.remove != '(':
                return False
            elif s == ']' and pilha_s.remove != '[':
                return False
            elif s == '}' and pilha_s.remove != '{':
                return False

    if pilha_s.vazia():
        return True
    else:
        return False


#as expressoes sao: [(x + y) * 2] = 0; [(x + y] * 2) = 0; [(x + y * 2) = 0

string=list(input("Digite expressão: "))
print(verifica(string))
