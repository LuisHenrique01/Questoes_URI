def main():
    while True:
        try:
            l= list(input().split())
            v = int(l[0])
            t = int(l[1])
            print((v*t)*2)
        except EOFError:
            break

if __name__ == "__main__":
    main()