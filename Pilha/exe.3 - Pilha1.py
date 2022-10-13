#Verificação de expressão aritmética

from classe_pilha import Pilha

pilha = Pilha()

def verifica(entrada):
    for c in entrada:
        if c == '(' or c == '[' or c =='{':
            pilha.insere(c)
        elif c == ')' or c == ']' or c == '}':
            if pilha.vazia():
                return False
            if c == ')' and pilha.remove() != '(':
                return False
            elif c == ']' and pilha.remove() != '[':
                return False
            elif c == '}' and pilha.remove != '{':
                return False

    if pilha.vazia():
        return True
    else:
        return False

string=(input("Digite expressão: "))

print(verifica(string))
