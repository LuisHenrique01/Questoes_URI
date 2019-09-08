def main():
    while True:
        d, n = map(str, input().split())
        if d == '0' and n == '0': break
        num = '0'
        for i in range(0, len(n)):
            if n[i] != d:
                num = num + n[i]
        print(int(num))

main()