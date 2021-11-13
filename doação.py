total = 0
reais = 2.5
c = 0
d = float(input())
while d != -1:
    total += d
    d = float(input())
    c = reais * total
print(f'VC$ {total:.2f}')
print(f'R$ {c:.2f}')
