import random
def main():
    n = int(input())
    for i in range(n):
        nome = input()
        nivel = float(input())
        lista = list(map(float, input().split()))
        lista.sort()
        soma = 0
        for i in range(1, len(lista)-1, 1): soma += lista[i]
        print("%s %.2f"%(nome, soma*nivel))


if __name__ == "__main__":
    main()