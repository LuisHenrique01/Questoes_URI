def main():
    while True:
        try:
            a, b, c = tuple(map(int, input().split()))
            if ((a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2)) and mdc_e_1(a, b, c):
                print('tripla pitagorica primitiva')
            elif ((a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2)) and not(mdc_e_1(a, b, c)):
                print('tripla pitagorica')
            else:
                print('tripla')
        except EOFError:
            break
        
        
def mdc_e_1(a, b, c):
    m = min([a, b, c])
    for i in range(2, m):
        if a % i == 0 and b % i == 0 and c % i == 0:
            return False
    return True

main()