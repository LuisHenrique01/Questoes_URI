def main():
    pares = []
    impares = []
    for i in range(15):
        num = int(input())
        if num % 2 == 0:
            pares += [num]
        else:
            impares += [num]
        if len(pares) == 5:
            mostra_nuns('par', pares)
            pares = []
        if len(impares) == 5:
            mostra_nuns('impar', impares)
            impares = []
    mostra_nuns('impar', impares)
    mostra_nuns('par', pares)


def mostra_nuns(texto, lista):
    j = 0
    for i in range(len(lista)):
        print('%s[%i] = %i'%(texto, j, lista[i]))
        j += 1
        if j > 4:
            j = 0


if __name__ == "__main__":
    main()
