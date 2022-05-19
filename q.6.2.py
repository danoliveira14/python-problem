def pede_numeros():
    cont = 1
    numeros = []
    while cont != 0:
        numero = input()
        if numero == '':
            cont -= 1
        else:
            n = float(numero)
            numeros.append(n)
    return numeros


def calcula_media(s):
    global media
    cont = 1
    i = 1
    x =
    while cont < len(s):
        soma = s[0] + s[i]
        soma += s[i]
        i += 1
        cont += 1
        if i == len(s):
            media = soma / len(s)
    return media


n = pede_numeros()
me = calcula_media(n)
print(me)
