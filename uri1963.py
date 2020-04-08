def main():
    a, b = list(map(float, input().split()))
    print("%.2f%%"%(((b-a)*100)/a))


main()