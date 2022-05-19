# receber numeros inteiros, e tornar uma lista
# receber comandos do usuario:
# adicionar: inclui o código de um novo produto à lista;
# remover: remove o código de um produto da lista;
# exibir: exibe os itens da lista em ordem crescente;
# encerrar: exibe os itens da lista, de modo idêntico
# ao comando exibir, e encerra o programa.
# adicionar ou remover itens da lista
# entrada se encerrara com o comando "encerrar".
# exibir a lista adicionada no input com o comando "exibir"
# a mensagem "código n não encontrado" quando o usuario
#  tenta remover o que não existe na lista

def converte(lista):
    n = []
    for i in lista:
        n.append(int(i))
    return n


itens = input().split()
comandos = []
contador = 1


while contador > 0:
    comandos = input().split()
    numeros = converte(itens)

    if comandos[0] == "adicionar":
        itens.append(comandos[1])

    elif comandos[0] == "exibir":
        x = len(numeros)
        converte(numeros)
        numeros.sort()
        print(*numeros)

    elif comandos[0] == "remover":
        if comandos[1] in itens:
            itens.remove(comandos[1])
        else:
            print(f'código {comandos[1]} não encontrado')

    elif comandos[0] == "encerrar":
        x = len(numeros)
        converte(numeros)
        numeros.sort()
        print(*numeros)

        contador -= 1
        break
