def main():
    input()
    hits = list(map(int, input().split()))
    algoz = hits.index(min(hits))
    print("%s"%(algoz + 1))


if __name__ == "__main__":
    main()