def main():
    x, y = list(map(int, input().split()))  

    q = x // y
    r= x % y
    if r < 0:
        if q < 0:
            q = q - 1
        if q > 0:
            q = q + 1
        r = x-(y*q)

    print("%d %d"%(q, r))


if __name__ == "__main__":
    main()