def main():
    operacao = input()
    vetor = criar_vetor(12)
    matriz = criar_matriz(12, vetor)
    matriz = preencher_matriz(matriz, 12)
    if operacao == 'S':
        soma = soma_ele_linha(matriz)
        print("%.1f"%soma)
    else:
        media = media_ele_linha(matriz)
        print("%.1f"%media)


def preencher_matriz(matriz, tamanho_linha):
    for i in range(len(matriz)):
        matriz[i] = preencher_vetor(criar_vetor(12))
    return matriz

def criar_matriz(numero_linhas, vetor):
    matriz = [vetor]*numero_linhas
    return matriz


def criar_vetor(tamanho_linha):
    return [0]*tamanho_linha


def preencher_vetor(vetor):
    for i in range(len(vetor)):
        vetor[i] = float(input())
    return vetor


def soma_ele_linha(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j > i:
                soma = soma + matriz[i][j]

    return soma


def media_ele_linha(matriz):
    soma = 0
    elementos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j > i:
                soma = soma + matriz[i][j]
                elementos += 1

    return soma / elementos


main()