def abaixo(n1, n2):
    n = 0
    while n < len(n1):
        if n1[n] < n2:
            print(n1[n])
        n += 1


count = 1
abaixo_media = []
lista = []
i = 0
c = 0

while count != 0:
    segundos = int(input())
    if segundos > 0:
        lista.append(segundos)

    elif segundos < 0:
        media = sum(lista) / len(lista)
        print(f"MEDIA: {media:.2f}")
        inteiros = int(media)
        abaixo(lista, inteiros)
        count -= 1
