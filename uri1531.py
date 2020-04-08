def main():
    while True:
        try:
            n, m = list(map(int, input().split()))
            print(fibonacci(n) % m)
        except EOFError:
            break

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


main()