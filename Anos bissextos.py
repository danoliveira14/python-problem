inicio = int(input())
fim = int(input())

contador = 0

while inicio <= fim:
    if inicio % 400 == 0 or (inicio % 4 == 0 and inicio % 100 != 0):
        print(inicio)
        inicio += 4
        contador += 1

    else:
        inicio += 1

print('bissextos:', contador)
