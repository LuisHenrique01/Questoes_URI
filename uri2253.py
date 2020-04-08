def main():
    while True:
        try:
            senha = input()
            num = False
            ma = False
            mi = False
            eh_l = True
            if len(senha) < 6 or len(senha) > 32:
                print('Senha invalida.')
            else:
                for i in range(len(senha)):
                    if ord(senha[i]) > 47 and ord(senha[i]) < 58:
                        num = True
                    elif ord(senha[i]) > 64 and ord(senha[i]) < 91:
                        ma = True
                    elif ord(senha[i]) > 96 and ord(senha[i]) < 123:
                        mi = True
                    else:
                        eh_l = False
                if num and mi and ma and eh_l:
                    print('Senha valida.')
                else:
                    print('Senha invalida.')
        except EOFError:
            break


if __name__ == "__main__":
    main()