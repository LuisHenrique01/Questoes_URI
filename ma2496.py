for _ in range(int(input())):
    n = int(input())
    palavra = list(input())
    ordem = sorted(palavra)
    letrasErradas = []
    posicoeLetrasErradas = []
    for i, letra in enumerate(palavra):
        if letra != ordem[i]:
            letrasErradas.append(letra)
            posicoeLetrasErradas.append(i)
    if len(letrasErradas) == 2:
        palavra[posicoeLetrasErradas[0]] = letrasErradas[1]
        palavra[posicoeLetrasErradas[1]] = letrasErradas[0]
        if ''.join(palavra) == ''.join(ordem):
            print("There are the chance.")
        else:
            print("There aren't the chance.")
    else:
        print("There aren't the chance.")