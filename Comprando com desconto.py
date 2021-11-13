
preço = float(input())
vendas = int(input())

preço = preço * vendas
desconto = vendas + 10
preço_final = preço - (preço * desconto / 100)

print(f'{preço:.2f}')
print(f"{preço_final:.2f}")