def main():
    for i in range(int(input())): print("%s"%(retorna_todas_iniciais(input())))


def retorna_todas_iniciais(nome):
    iniciais = ''
    anterior = ' '
    for i in range(len(nome)):
        if nome[i] != ' ' and anterior == ' ':
            iniciais = iniciais + nome[i]
        anterior = nome[i]
    return iniciais


if __name__ == "__main__":
    main()