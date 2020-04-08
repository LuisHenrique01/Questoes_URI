def main():
    for _ in range(int(input())):
        codigo = input()
        crip = ''
        for i in range(len(codigo)):
            if ord(codigo[i]) > 96 and ord(codigo[i]) < 123:
                crip = crip + codigo[i] 
        print(crip[::-1])


if __name__ == "__main__":
    main()
