def main():
    for i in range(int(input())):
        texto = input()
        tags = [texto[i] for i in range(len(texto)) if texto[i] == '<' or texto[i] == '>']
        abrir = tags.count("<")
        fechar = tags.count(">")
        if abrir == fechar:
            print("Successful !!")
        else:
            print("error")


if __name__ == "__main__":
    main()