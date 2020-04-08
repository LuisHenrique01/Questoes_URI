def main():
    lista = []
    while True:
        try:
            joia = input()
            if not joia in lista:
                lista.append(joia)
        except EOFError:
            break
    print("%d"%len(lista))


if __name__ == "__main__":
    main()