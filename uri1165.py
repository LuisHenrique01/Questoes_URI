def main():
    n = int(input())
    i = 1
    while i <= n:
        num = int(input())
        j = 2
        e_primo = False
        while j < num:
            if num % j == 0:
                e_primo = True
                break
            else:
                e_primo = False
            j += 1
        if e_primo:
            print('%i nao eh primo'%num)
        else:
            print('%i eh primo'%num)
        i += 1


if __name__ == "__main__":
    main()