def main():
    maior = ''
    while True:
        frase = input()
        if frase == '0': break
        cont_caracter = ''
        cont = 0
        palavra = ''
        for i in range(len(frase)):
            if (len(frase) - 1) == i:
                cont_caracter = cont_caracter + '-' + str(cont+1)
                palavra = palavra + frase[i]
                if len(maior) <= len(palavra):
                    maior = palavra

            if frase[i] == ' ':
                cont_caracter = cont_caracter + '-' + str(cont)
                if len(maior) <= len(palavra):
                    maior = palavra
                cont = 0
                palavra = ''
            else:
                palavra = palavra + frase[i]
                cont += 1

        print(cont_caracter[1::])
    print()
    print('The biggest word: %s'%maior)      


if __name__ == "__main__":
    main()