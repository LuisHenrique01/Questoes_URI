def main():
    while True:
        try:
            m, n = list(map(int, input().split()))
            fatm = 1
            fatn = 1
            for i in range(m, 0, -1):
                fatm *= i
            for j in range(n, 0, -1):
                fatn *= j
            print(fatm+fatn)
        except EOFError:
            break


main()