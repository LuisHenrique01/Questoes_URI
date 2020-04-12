def main():
    h, t, f = list(map(int, input().split()))
    print("%d"%(formata(formata(h, t), f)))


def formata(h, n):
    if h+n < 24 and h+n >= 0:
        return h+n
    elif h+n < 0:
        return 24 + (h+n)
    else:
        return (h+n) - 24
    

if __name__ == "__main__":
    main()