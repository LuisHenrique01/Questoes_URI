def main():
    while True:
        try:
            new_texto = ''
            contaster = 0
            contander = 0
            texto = input()
            for i in range(len(texto)):
                if texto[i] == '_':
                    contaster += 1
                    if contaster % 2 != 0:
                        new_texto = new_texto + '<i>'
                    else:
                        new_texto = new_texto + '</i>'
                elif texto[i] == '*':
                    contander += 1
                    if contander % 2 != 0:
                        new_texto = new_texto + '<b>'
                    else:
                        new_texto = new_texto + '</b>'
                else:
                    new_texto = new_texto + texto[i]
            print(new_texto)

        except EOFError:
            break


if __name__ == "__main__":
    main()