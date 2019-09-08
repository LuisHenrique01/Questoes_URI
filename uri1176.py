def main():
    for i in range(int(input())):
        n = int(input())
        fib = fibonacci()
        print("Fib(%d) = %d"%(n, fib[n]))


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