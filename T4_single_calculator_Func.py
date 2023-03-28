def calculatorFunc(a,b,c):
    if b == "+":
        return a+c
    elif b == "-":
        return abs(a-c)
    elif b == "*":
        return a*c
    elif b == "/":
        return a/c
    
a, b, c = input("Enter an expression : ").split()
result = calculatorFunc(int(a),b,int(c))

print(result)