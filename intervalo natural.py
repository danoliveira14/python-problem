total = 0 # variável acumuladora

preco = float(input('preço do item: '))

while preco != -1:
    total += preco
    preco = float(input('preço do item: '))

print(f'Total da compra: R$ {total:.2f}')