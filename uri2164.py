def main():
    n = int(input())
    fib = ((((1 + (5**0.5))/2)**n) - (((1 - (5**0.5))/2)**n)) / (5**0.5)
    print("%.1f"%fib)


main()

