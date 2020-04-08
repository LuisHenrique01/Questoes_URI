 def main():
    while True:
        try:
            m, n = list(map(int, input().split()))
            matriz = [list(map(int, input().split())) for i in range(m)]
            litros = sum([sum(matriz[i]) for i in range(m)])
            print("%d saca(s) e %d litro(s)"%(litros//60, litros%60))
        except EOFError:
            break


main()