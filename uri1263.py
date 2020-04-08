def main():
    while True:
        try:
            iniciais = retorna_todas_iniciais(input().lower())
            aliteracoes = 0
            anterior = ''
            for i in range(len(iniciais)-1):
                if iniciais[i] == iniciais[i+1] and iniciais[i] != anterior:
                    aliteracoes += 1
                anterior = iniciais[i]
            print(aliteracoes)
        except EOFError:
            break


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