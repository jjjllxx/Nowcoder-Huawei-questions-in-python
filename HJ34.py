str1 = input()
list1, str2 = [], ''
for i in str1:
    list1.append(i)
list1.sort()
str2 = ''.join(list1)
print(str2)
