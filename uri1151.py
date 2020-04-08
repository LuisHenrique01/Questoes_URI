def main():
    n = int(input())
    i = 3
    penultimo = 0
    ultimo = 1
    atual = 1
    print('0 1', end = ' ')
    while i <= n:
        atual = penultimo + ultimo
        penultimo = ultimo
        ultimo = atual
        if i != n:
            print(atual, end = ' ')
        else:
            print(atual)
        i += 1


if __name__ == "__main__":
    main()