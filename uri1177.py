def main():
    t = int(input())
    j = 0
    for i in range(1000):
        if j < t:
            print("N[%d] = %d"%(i, j))
        else:
            j = 0
            print("N[%d] = %d"%(i, j))
        j += 1


if __name__ == "__main__":
    main()