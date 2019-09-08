def main():
    for _ in range(int(input())):
        inicial, repeticoes = list(map(int, input().split()))
        resu = 0
        for i in range(repeticoes):
            if inicial % 2 == 0:
                resu += inicial + 1
                inicial += 3
            else:
                resu += inicial
                inicial += 2
        print("%d"%resu)


if __name__ == "__main__":
    main()