"""
File: HJ55.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2021-07-30 00:20:46
Function:


"""
num = int(input())
n = 0
for i in range(1, num+1):
    if i % 7 == 0 or '7' in str(i):
        n += 1
print(n)
