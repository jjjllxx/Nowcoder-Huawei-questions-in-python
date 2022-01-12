"""
File: HJ9.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2021-07-30 00:34:11
Function:


"""
num = input()
str1 = ''
for i in num[::-1]:
    if i not in str1:
        str1 += i
print(str1)
