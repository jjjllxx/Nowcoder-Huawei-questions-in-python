"""
File: HJ10.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2021-07-29 23:29:51
Function:


"""
str1 = input()
list1 = []
for i in str1:
    if i not in list1 and (0 <= ord(i) <= 127):
        list1.append(i)
print(len(list1))
