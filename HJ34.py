"""
File: HJ34.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2021-07-29 23:48:40
Function:


"""
str1 = input()
list1, str2 = [], ''
for i in str1:
    list1.append(i)
list1.sort()
str2 = ''.join(list1)
print(str2)
