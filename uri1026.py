def main():
    while True:
        try:
            num_1, num_2 = map(int, input().split())
            print(num_1^num_2)
        except EOFError:
            break


if __name__ == "__main__":
    main()