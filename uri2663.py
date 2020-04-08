import random
def main():
    n = int(input())
    k = int(input())
    vetor = [int(input()) for i in range(n)]
    vetor.sort(reverse=True)
    comp = k
    for i in range(k, len(vetor), 1):
        if vetor[i] == vetor[k-1]:
            comp += 1
    print("%d"%comp)


if __name__ == "__main__":
    main()