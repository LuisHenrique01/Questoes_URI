def main():
    resultados = []
    linhas = int(input())
    matriz = [list(map(int, input().split())) for i in range(linhas)]
<<<<<<< HEAD
    for i in range(len(matriz)):
        resultados.append(sum(matriz[i]))
    soma_coluna = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            soma_coluna += matriz[j][i]
        resultados.append(soma_coluna)
        soma_coluna = 0
=======

    for i in range(len(matriz)):
        resultados.append(sum(matriz[i]))
    
    soma_coluna = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                soma_coluna += matriz[i][i]
                break
    resultados.append(soma_coluna)
>>>>>>> 1e6078b5744e52bdf2f5004ed0f7e84fdb0a2350

    resultados.append(soma_ele_linha_prin(matriz))
    resultados.append(soma_ele_linha_sec(matriz))
    if len(set(resultados)) == 1:
        print("%d"%resultados[0])
    else:
        print("-1")
    

def soma_ele_linha_prin(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if not(j > i and j < i):
                soma = soma + matriz[i][j]
                break

    return soma


def soma_ele_linha_sec(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if not(j + i < len(matriz) - 1 and j + i > len(matriz) - 1):
                soma = soma + matriz[i][j]
                break
    return soma


if __name__ == "__main__":
    main()