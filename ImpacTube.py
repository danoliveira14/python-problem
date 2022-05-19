def bonus(lista, n1, n2):
    if lista[3] == "não":
        c1 = int(lista[1])
        c2 = float(lista[2])
        bon = (c1 // 1000) * n1 + c2
        return print(f"{lista[0]}: R$ {bon:.2f}")

    elif lista[3] == "sim":
        c1 = int(lista[1])
        c2 = float(lista[2])
        bon = (c1 // 1000) * n2 + c2
        return print(f"{lista[0]}: R$ {bon:.2f}")


def exiba():
    print(5 * "-")
    print("BÔNUS")
    print(5 * "-")


A = int(input())
count = 1
canais = []
i = 0


while count <= A:
    canal = input().split(";")
    canais.append(canal)
    count += 1
    c = len(canais)
    if A == c:
        X = float(input())
        Y = float(input())
        exiba()
        while c > 0:
            bonus(canais[i], Y, X)
            c -= 1
            i += 1
