def main():
    while True:
        try:
            enunciado = input()
            list_enun = my_split(enunciado, ' ')
            palavras = 0
            letras = 0
            for i in range(len(list_enun)):
                if eh_palavra(list_enun[i]):
                    if list_enun[i][len(list_enun[i]) - 1] == '.':
                        palavras += 1
                        letras += len(list_enun[i]) - 1
                    else:
                        palavras += 1
                        letras += len(list_enun[i])
            if palavras != 0:
                media = letras//palavras
                if media <= 3:
                    print('250')
                elif media < 6:
                    print('500')
                else:
                    print('1000')
            else:
                print('250')

        except EOFError:
            break


def my_split(valores, splitador):
    vetor = []
    valor = ''
    for i in range(len(valores)):
        if valores[i] != splitador:
            valor += valores[i]
            if len(valores) - 1 == i:
                vetor += [valor]
        else:
            vetor += [valor]
            valor = ''
    return vetor


def eh_palavra(palavra):
    ultimo_index = len(palavra) - 1
    if ultimo_index < 0:
        return False
    elif palavra[0] == '.':
        return False
    elif ultimo_index == 0 and eh_numero(palavra):
        return False
    elif palavra[ultimo_index] == '.' and palavra[ultimo_index-1] == '.':
        return False
    for i in range(len(palavra)):
        if eh_numero(palavra[i]):
            return False
        elif i != ultimo_index and palavra[i] == '.':
            return False
    return True


def eh_numero(caracter):
    if ord(caracter) > 47 and ord(caracter) < 58:
        return True
    else:
        return False

main()