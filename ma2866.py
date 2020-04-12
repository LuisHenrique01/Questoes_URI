for i in range(int(input())):
    crip = input()
    text = [i for i in list(crip) if ord(i) >= 97 and ord(i) <= 122]
    print("%s"%(''.join(text[::-1])))