def preencher_matriz(matriz, tamanho_linha):
    for i in range(len(matriz)):
        matriz[i] = preencher_vetor(criar_vetor(tamanho_linha))
    return matriz

def criar_matriz(vetor, numero_linhas,):
    matriz = [vetor]*numero_linhas
    return matriz


def criar_vetor(tamanho_linha):
    return [0]*tamanho_linha


def preencher_vetor(vetor):
    for i in range(len(vetor)):
        vetor[i] = float(input())
    return vetor


def soma_ele_linha(matriz, linha):
    soma = 0
    for i in range(len(matriz[linha])):
        soma += matriz[linha][i]
    return soma


def mutiplica_ele_linha(matriz, linha):
    soma = 0
    for i in range(len(matriz[linha])):
        soma *= matriz[linha][i]
    return soma



def soma_ele_linha(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j > i and j + i > len(matriz) - 1:
                soma = soma + matriz[i][j]

    return soma


def media_ele_linha(matriz):
    soma = 0
    elementos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j > i and j + i > len(matriz) - 1:
                soma = soma + matriz[i][j]
                elementos += 1

    return soma / elementos


def mostrar_matriz(matriz, msg="Essa é a matriz!"):
    print(msg)
    for i in range(len(matriz)):
        print(" ", end = ' ')
        for j in range(len(matriz[i])):
            if j != len(matriz[i]) - 1:
                print("%d"%matriz[i][j], end = '   ')
            else:
                print("%d"%matriz[i][j])