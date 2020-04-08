def main():
    while True:
        n, m = list(map(str, input().split()))
        if n == '0' and m == '0': break
        vai = 0
        cont = 0
        if len(n) > len(m):
            maior = len(n)
        else:
            maior = len(m)

        for _ in range(maior):
            if len(n) < maior:
                n = '0' + n
            if len(m) < maior: 
                m = '0' + m

        for i in range(maior-1, -1, -1):
            if int(n[i]) + int(m[i]) + vai > 9:
                vai = 1
                cont += 1
            else:
                vai = 0

        if cont == 0:
            print("No carry operation.")
        elif cont == 1:
            print("%d carry operation."%cont)
        else:
            print("%d carry operations."%cont)


main()