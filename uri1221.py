def main():
    for _ in range(int(input())):
        numero = int(input())
        div = 0
        parada = int(numero**0.5) + 1
        for i in range(1, parada, 1):
            if numero % i == 0:
                div += 1
                if div > 1:
                    break
        if numero == 1 or div > 1:
            print('Not Prime')
        else:
            print('Prime')

if __name__ == "__main__":
    main()