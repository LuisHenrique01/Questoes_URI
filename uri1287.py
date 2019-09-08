def main():
    while True:
        try:
            string = input()
            print(retona_numero(string))
        except EOFError:
            break

def retona_numero(string):
    new = ''
    for i in range(len(string)):
        if string[i] != ' ' and string[i] != ',':
            if string[i] == 'o' or string[i] == 'O':
                new = new + '0'
            elif string[i] == 'l':
                new = new + '1'
            else:
                new = new + string[i]
    try:
        if int(new) <= 2147483647:
            return int(new)
        else:
            return 'error'
    except ValueError:
        return 'error'


if __name__ == "__main__":
    main()