def main():
    i = 0
    while True:
        try:
            ano = int(input())
            if i != 0: print()
            if e_bixeto(ano):
                print("This is leap year.")
            if ano % 15 == 0:
                print("This is huluculu festival year.")
            if e_bixeto(ano) and ano % 55 == 0:
                print("This is bulukulu festival year.")
            if not(e_bixeto(ano)) and not(ano % 15 == 0) and not(e_bixeto(ano) and ano % 55 == 0):
                print("This is an ordinary year.")
            i = 1
        except EOFError:
            break

def e_bixeto(ano):
    if ano % 4 == 0 and ano % 100 != 0:
        return True
    elif ano % 400 == 0:
        return True
    else:
        return False


main()