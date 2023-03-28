vowels = ['a', 'e', 'i', 'o', 'u']
new_list = []
result = ''
str = input("Enter any string : ")
for i in str:
    if i in vowels:
        new_list.append("1")
    else:
        new_list.append("0")

result = result.join(new_list)
print(result)