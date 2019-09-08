def main():
    n = int(input())
    i = 1
    while i <= n:
        num = int(input())
        j = 1
        soma = 0
        while j < num:
            if num % j == 0:
                soma += j
            j += 1
        if soma == num:
            print('%i eh perfeito'%num)
        else:
            print('%i nao eh perfeito'%num)
        i += 1
                


if __name__ == "__main__":
    main()