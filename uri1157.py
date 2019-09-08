def main():
    n = int(input())
    for i in range(1, n+1, 1):
        if n % i == 0:
            print("%d"%i)


if __name__ == "__main__":
    main()