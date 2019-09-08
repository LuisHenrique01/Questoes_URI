def main():
    a = int(input())
    vetor = input().split()
    soma = 0
    for i in range(len(vetor)):
        soma += int(vetor[i]) - 1
    print("%d"%soma)


main()