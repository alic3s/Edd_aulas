'''def fatorial(n):
    if n == 0:
        fat = 1
    else:
        fat = n * fatorial(n - 1)
    return fat


def potencia(n):
    if n == 0:
        return 1
    else:
        print(n, "* potência(", n-1, ")")
        return 2 * potencia(n-1)

print(potencia(8))


def fibonacci(n):
    if n < 0:
        return f'Inválido'
    elif n == 1 or n == 2:
        return 1
    else:
        print(n, 'na sequência de fibonacci(', n - 1,')','+ (' , n - 2, ')')
        return (fibonacci(n - 1) + fibonacci(n - 2))

print(fibonacci(6))'''

#sei essa merda não
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(9))
