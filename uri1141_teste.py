import time

def main():
    inicio = time.time()
    while True:
        strings = []
        sequencias = []
        sequencia = 0
        valores_a_ler = int(input())
        if valores_a_ler == 0: break
        for _ in range(0, valores_a_ler):
            strings.append(input())
        strings.sort()
        for i in range(0, len(strings)):
            index = i
            for j in range(0, len(strings)):
                if strings[index] in strings[j]:
                    index = j
                    sequencia += 1
                    

            sequencias.append(sequencia)
            sequencia = 0
        print(max(sequencias))
    print(time.time() - inicio)


if __name__ == "__main__":
    main()
        