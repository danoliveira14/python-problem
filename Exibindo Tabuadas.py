A = int(input())
B = int(input())

def tabu(n):
    for count in range(10):
        print("%d x %d = %d" % (n, count+1, n*(count+1)))


if A <= B:
    while A <= B:
        tabu(A)
        print(10*"-")
        A += 1

else:
    print("Nenhuma tabuada no intervalo!")