def main():
    while True:
        try:
            frase = input()
            ant_caracter = ' '
            new_str = ''
            for i in range(0, len(frase)):
                if e_letra(frase[i]) and not(ord(ant_caracter) > 64 and ord(ant_caracter) < 91):
                    new_str = new_str + frase[i].upper()
                    ant_caracter = frase[i].upper()
                elif e_letra(frase[i]) and (ord(ant_caracter) > 64 and ord(ant_caracter) < 91): 
                    new_str = new_str + frase[i].lower()
                    ant_caracter = frase[i].lower()
                else:
                    new_str = new_str + frase[i]
            print(new_str)
        except EOFError:
            break


def e_letra(caracter):
    return (ord(caracter) > 64 and ord(caracter) < 91) or (ord(caracter) > 96 and ord(caracter) < 123)
        
            
main()