def main():
    while True:
        try:
            a = input()
            b = input()
            if len(a) > len(b):
                maior = a 
                menor = b
            else:
                maior = b
                menor = a 
            vetor = [maior[i] for i in range(len(maior)) if maior[i] in menor and maior[i] != ' ']
            vet = set(vetor)
            print(vet)
            print(vetor)
            print('%d'%len(vet))
        except EOFError:
            break


if __name__ == "__main__":
    main()
        