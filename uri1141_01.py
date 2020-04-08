def main():
    while True:
        strings = []
        sequencias = []
        sequencia = 0
        valores_a_ler = int(input())

        if valores_a_ler == 0: break
        strings = [input() for _ in range(valores_a_ler)]
        strings.sort(key = len)
        index = 0
        for j in range(0, len(strings)):
            if strings[index] in strings[j]:
                index = j
                sequencia += 1        
        sequencias.append(sequencia)
        sequencia = 0
        print(max(sequencias))


if __name__ == "__main__":
    main()