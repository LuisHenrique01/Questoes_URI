def main():
    for _ in range(int(input())):
        a, b = list(map(int, input().split()))
        s = "%d"%a**b
        print("%d"%len(s))


main()