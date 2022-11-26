def fatorial(n):
    if n == 0:
        fat = 1
    else:
        fat = n * fatorial(n - 1)
    return fat


def potencia(n):
    if n == 0:
        return 1
    else:
        print(n, "* fatorial(", n-1, ")")
        return 2 * potencia(n-1)

print(potencia(4))
