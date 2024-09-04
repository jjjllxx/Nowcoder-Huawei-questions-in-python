num = input()
str1 = ''
for i in num[::-1]:
    if i not in str1:
        str1 += i
print(str1)
