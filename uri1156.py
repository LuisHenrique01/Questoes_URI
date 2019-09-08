def main():
    i = 1
    soma = 0
    j = 1
    while i <= 39:
        soma += i/j
        i += 2
        j *= 2
    print('%.2f'%soma)


if __name__ == "__main__":
    main()