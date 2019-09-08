def main():
    while True:
        try:
            palavras, linhas_paginas, caracter_linha = map(int, input().split())
            frase = input()
            caracteres = 0
            linhas = 0
            for i in range(0, len(frase), caracter_linha):
                for j in range(caracter_linha):
                    if i+j == caracter_linha-1:
                        if frase[index_ant] == ' ':
                            linhas += 1
                    else:
                        if frase[i+j] == ' ':
                            index_ant = i+j
            print(linhas//linhas_paginas)
        except EOFError:
            break


main()