"""
File: HJ99.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2021-07-30 00:43:59
Function:


"""
n = int(input())
num = 0
for i in range(n + 1):
    if i == i ** 2 % (10**len(str(i))):
        num += 1
print(num)
