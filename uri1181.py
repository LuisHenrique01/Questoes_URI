def main():
    linha = int(input())
    operacao = input()
    vetor = criar_vetor(12)
    matriz = criar_matriz(12, vetor)
    matriz = preencher_matriz(matriz, 12)
    if operacao == 'S':
        soma = soma_ele_linha(matriz, linha)
        print("%.1f"%soma)
    else:
        media = media_ele_linha(matriz, linha)
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


def soma_ele_linha(matriz, linha):
    soma = 0
    for i in range(len(matriz[linha])):
        soma += matriz[linha][i]
    return soma


def media_ele_linha(matriz, linha):
    media = soma_ele_linha(matriz, linha) / len(matriz[linha])
    return media


main()