def largestNumberBetween3(a,b,c):
    if a>b:
        if a>c:
            print(a)
        else:
            print(c)
    else:
        if b>c:
            print(b)
        else:
            print(c)

a, b, c = input("Enter three numbers : ").split()
largestNumberBetween3(a,b,c)