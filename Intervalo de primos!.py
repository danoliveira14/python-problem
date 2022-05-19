from math import sqrt
from itertools import count, islice


def prime(n1):
    if n1 < 2:
        return False

    for c in islice(count(2), int(sqrt(n1) - 1)):
        if n1 % c == 0:
            return False

    return True


inicio = int(input())
fim = int(input())
primos = 0

while inicio <= fim:
    prime(inicio)

    if not prime(inicio):
        inicio += 1

    else:
        print(inicio)
        inicio += 1
        primos += 1

print('primos:', primos)
