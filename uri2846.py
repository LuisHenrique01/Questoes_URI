def main():
    fibnot = int(input())
    fib = fibonacci()
    for i in range(1, fib[len(fib) - 1], 1):
        if not i in fib:
            fibnot -= 1
        if fibnot == 0:
            print("%d"%i)
            break


def fibonacci():
    tabela=[0,1]
    anterior=0
    atual=1
    for i in range(60):
        tnp = atual+anterior
        tabela.append(tnp)
        anterior=atual
        atual=tnp
    return tabela


if __name__ == "__main__":
    main()