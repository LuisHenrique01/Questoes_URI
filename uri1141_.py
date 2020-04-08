def main():
    while True:
        strings = []
        sequencias = []
        sequencia = 0
        valores_a_ler = int(input())

        if valores_a_ler == 0: break
        for _ in range(0, valores_a_ler, 1):
            strings.append(input())
        strings.sort(key=len)
        index = 0
        while index < 3:
            for j in range(0, len(strings), 1):
                if strings[index] in strings[j]:
                    index = j
                    sequencia += 1        
            sequencias.append(sequencia)
            sequencia = 0
            index = index + 1
        print("%i"%max(sequencias)) 


if __name__ == "__main__":
    main()
        