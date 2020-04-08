def main():
    while True:
        num = int(input())
        i = 1
        soma = 0
        if num == 0:
            break
        while i <= 5:
            if num % 2 == 0:
                soma += num
                i += 1
            num += 1
        print(soma)


if __name__ == "__main__":
    main()