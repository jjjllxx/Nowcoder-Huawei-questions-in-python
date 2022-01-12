"""
File: HJ37.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2021-07-29 16:35:54
Function:


"""
month = int(input())
num = [1, 1]
for i in range(2, month):
    num.append(num[i-2]+num[i-1])
print(num[month-1])
