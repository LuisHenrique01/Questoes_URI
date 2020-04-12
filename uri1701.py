def fibona(n):
    return int(((((1 + (5**0.5))/2)**n) - (((1 - (5**0.5))/2)**n)) / (5**0.5))

def main():
    while True:
        a, b, n = tuple(map(int, input().split(' ')))
        if a == b and b == n and n == 0:break
        re = 0
        for i in range(n):
            re += fibona(a) * fibona(b)
            a += 1
            b += 1
        re = int(re%1000000007)
        print(re)
        

       
if __name__ == "__main__":
    main()