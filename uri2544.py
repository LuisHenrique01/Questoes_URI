def main():
    while True:
        try:
            clones = int(input())
            i = 2
            ninjas = 0
            while i <= clones:
                ninjas += 1
                i *= 2
            print(ninjas) 
        except EOFError:
            break


if __name__ == "__main__":
    main()