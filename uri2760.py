def main():
    while True:
        try:
            a = input()
            b = input()
            c = input()
            passo_5 = a+b+c
            passo_6 = b+c+a
            passo_7 = c+a+b
            passo_8 = a[:10:1]+b[:10:1]+c[:10:1]
            print("%s"%passo_5)
            print("%s"%passo_6)
            print("%s"%passo_7)
            print("%s"%passo_8)
        except EOFError:
            break


if __name__ == "__main__":
    main()