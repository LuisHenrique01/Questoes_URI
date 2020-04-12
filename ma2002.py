def custo(x, y):
    valor = 0

    for i in range(min(x, y), max(x, y)+1):  # Fica de olho nesse 1
        valor = valor ^ i

    return valor

while True:
    try:
        linhas, colunas = tuple(map(int, input().split()))
        matriz = [list(map(int, input().split())) for i in range(linhas)]
        linhaAtu, columAtu = (0, 0)
        linhaFim, columFim = (linhas-1, colunas-1)
        custoT = 0
        while not(linhaAtu == linhaFim and columAtu == columFim):
            if columAtu == columFim:
                c = custo(matriz[linhaAtu][columAtu], matriz[linhaAtu+1][columAtu])
                linhaAtu += 1
            elif linhaAtu == linhaFim:
                c = custo(matriz[linhaAtu][columAtu], matriz[linhaAtu][columAtu+1])
                columAtu += 1
            else:
                if matriz[linhaAtu][columAtu+1] < matriz[linhaAtu+1][columAtu]:
                    c = custo(matriz[linhaAtu][columAtu], matriz[linhaAtu][columAtu+1])
                    columAtu += 1
                else:
                    c = custo(matriz[linhaAtu][columAtu], matriz[linhaAtu+1][columAtu])
                    linhaAtu += 1
            custoT += c
        print("%d"%custoT)
    except EOFError:
        break
    