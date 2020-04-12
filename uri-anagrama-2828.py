import math


def letrasRepetidas(palavra):
    letrasRepetidas = []
    quantidadeDeRepeticoes = []

    for i in range(len(palavra)):
        if palavra.count(palavra[i]) > 1 and palavra[i] not in letrasRepetidas:
            letrasRepetidas.append(palavra[i])
            quantidadeDeRepeticoes.append(palavra.count(palavra[i]))

    return quantidadeDeRepeticoes


def calculaDenominador(letrasRepetidas):
    denominador = 1

    for i in range(len(letrasRepetidas)):
        denominador = denominador * math.factorial(letrasRepetidas[i])

    return denominador


def main():
    palavra = input()

    letras = letrasRepetidas(palavra)

    if len(letras) == 0:
        quantidadeDeAnagramas = (math.factorial(len(palavra))) % ((10**9) + 7)
    else:
        numerador = math.factorial(len(palavra))
        denominador = calculaDenominador(letras)
        quantidadeDeAnagramas = (numerador/denominador) % ((10**9) + 7)

    print(int(quantidadeDeAnagramas))


if __name__ == "__main__":
    main()
