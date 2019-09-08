def main():
    for i in range(int(input())):
        m, n = list(map(int, input().split()))
        print(mdc(m, n))


def mdc(a , b):
    return a if b == 0 else mdc(b, a % b)


main()