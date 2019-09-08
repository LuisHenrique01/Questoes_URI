def main():
    input()
    nuns = list(map(int, input().split()))
    menor = nuns[0]
    index = 0
    for i in range(len(nuns)):
        if menor > nuns[i]:
            menor = nuns[i]
            index = i
    print("Menor valor: %d"%menor)
    print("Posicao: %d"%index)


if __name__ == "__main__":
    main()