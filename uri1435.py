def main():
    while True:
        n = int(input())
        if n == 0: break
        vetor = criar_vetor(n)
        matriz = criar_matriz(n, vetor)
        matriz = preencher_matriz(matriz, n)
        matriz = tratamento_matriz(matriz, n)
        mostrar_matriz(matriz)
        print()
        

def preencher_matriz(matriz, n):
    for i in range(len(matriz)):
        matriz[i] = preencher_vetor(criar_vetor(n))
    return matriz

def criar_matriz(numero_linhas, vetor):
    matriz = [vetor]*numero_linhas
    return matriz


def criar_vetor(tamanho_linha):
    return [0]*tamanho_linha


def preencher_vetor(vetor):
    for i in range(len(vetor)):
        vetor[i] = 1
    return vetor


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print(" ", end = ' ')
        for j in range(len(matriz[i])):
            if j != len(matriz[i]) - 1:
                print("%d"%matriz[i][j], end = '   ')
            else:
                print("%d"%matriz[i][j])

def tratamento_matriz(matriz, n):
    valor = 1
    cima = 0
    esq = 0
    baixo = n - 1
    direita = n - 1

    if (n % 2 == 0):
        meio = n / 2

    else:
        meio = (n + 1) / 2


    while (valor <= meio):
        i = esq
        while (i <= direita):
            matriz[cima][i] = valor
            matriz[baixo][i] = valor
            i+=1

        i = (cima + 1)
        while ( i < baixo):
            matriz[i][esq] = valor
            matriz[i][direita] = valor
            i+=1

        valor+=1
        cima+=1
        baixo-=1
        esq+=1
        direita-=1

    return matriz


main()

