def segunda_chance(lista1, lista2):
    n = 1
    i = 0
    while n <= len(lista1):
        if lista1[i] == 10.00 and lista2[i] == 10.00:
            print(f"-({'%03d' % n}) original: {lista1[i]:05.2f} | final: {lista1[i]:05.2f}")
            n += 1
            i += 1
        elif lista1[i] == 10 and lista2[i] < 10:
            print(f"-({'%03d' % n}) original: {lista1[i]:05.2f} | final: {lista1[i]:05.2f}")
            n += 1
            i += 1
        elif lista1[i] < 10.00 and lista2[i] < 10.00:
            print(f"-({'%03d' % n}) original: {lista1[i]:05.2f} | final: {lista1[i]:05.2f}")
            n += 1
            i += 1
        elif lista2[i] == 10.00:
            if lista1[i] <= 8:
                print(f"*({'%03d' % n}) original: {lista1[i]:05.2f} | final: {lista1[i] + 2:05.2f}")
                n += 1
                i += 1
            elif lista1[i] > 8:
                print(f"*({'%03d' % n}) original: {lista1[i]:05.2f} | final: 10.00")
                n += 1
                i += 1


def alteradas(lista1, lista2, Y):
    if len(lista1) == len(lista2):
        x = 0
        c = 0
        while x < len(lista1):
            if lista1[c] == 10.00 and lista2[c] == 10.00:
                Y -= 1
                x += 1
                c += 1
            else:
                x += 1
                c += 1
    return print("NOTAS ALTERADAS:", Y)


alunos = int(input())
notas = []
atividades = []
count = 1

while count != 0:
    nota = float(input())
    notas.append(nota)
    if len(notas) == alunos:
        n1 = 1
        while n1 <= len(notas):
            atividade = float(input())
            atividades.append(atividade)
            n1 += 1
            if len(atividades) == len(notas):
                alt = atividades.count(10)
                alteradas(notas, atividades, alt)
                segunda_chance(notas, atividades)
                count -= 1
