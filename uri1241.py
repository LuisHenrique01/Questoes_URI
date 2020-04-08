def main():
    while True:
        try:
            for i in range(int(input())):
                a, b = list(map(str, input().split()))
                if len(b) > len(a):
                    print('nao encaixa')
                else:
                    ta = len(a) - len(b)
                    if a[ta::] == b:
                        print('encaixa')
                    else:
                        print('nao encaixa')
        except EOFError:
            break        


if __name__ == "__main__":
    main()