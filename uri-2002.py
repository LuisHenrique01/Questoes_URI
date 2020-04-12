def adiciona_linha(matriz, entrada_linha):
    linha = []

    for i in entrada_linha:
        linha.append(int(i))

    matriz.append(linha)


def calcula_movimentacao(x, y):
    valor = 0

    for i in range(min(x, y), max(x, y)+1):  # Fica de olho nesse 1
        valor = valor ^ i

    return valor


def calcula_custo(matriz, linhas, colunas):
    custo = 0
    linha_atual = 0
    coluna_atual = 0
    custo_baixo_direita = 0
    valor_baixo_direita = 0
    valor_direita_baixo = 0
    elementos_baixo_direita = []
    elementos_direita_baixo = []

    # percorrer baixo -> direita
    while True:
        print(matriz)
        elemento_atual = matriz[coluna_atual][0]
        elementos_baixo_direita.append(elemento_atual)
        coluna_atual += 1
        if coluna_atual == colunas:
            while True:
                elemento_atual = matriz[coluna_atual-1][linha_atual+1]
                elementos_baixo_direita.append(elemento_atual)
                linha_atual += 1
                if linha_atual == (linhas-1):
                    break
            break

    for i in range(len(elementos_baixo_direita)-1):  # verifica esse 1
        valor_baixo_direita += calcula_movimentacao(elementos_baixo_direita[i],
                                                    elementos_baixo_direita[i+1])

    coluna_atual = 0
    linha_atual = 0

    while True:
        elemento_atual = matriz[0][linha_atual]
        elementos_direita_baixo.append(elemento_atual)
        linha_atual += 1
        if linha_atual == linhas:
            linha_atual = 0
            while True:
                elemento_atual = matriz[linha_atual+1][colunas-1]
                elementos_direita_baixo.append(elemento_atual)
                linha_atual += 1
                if linha_atual == (linhas-1):
                    break
            break

    for i in range(len(elementos_direita_baixo)-1):
        valor_direita_baixo += calcula_movimentacao(
            elementos_direita_baixo[i], elementos_direita_baixo[i+1])

    if valor_baixo_direita < valor_direita_baixo:
        return valor_baixo_direita

    return valor_direita_baixo


def main():

    while True:
        try:
            entrada_dimensoes_matriz = input().split()
            linhas, colunas = map(int, entrada_dimensoes_matriz)

            matriz = []

            for i in range(linhas):
                entrada_linha = input().split()
                adiciona_linha(matriz, entrada_linha)
            custo = calcula_custo(matriz, linhas, colunas)

            print(custo)

        except EOFError:
            break


if __name__ == "__main__":
    main()
