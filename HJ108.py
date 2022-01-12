"""
File: HJ108.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2021-07-29 23:04:55
Function:


"""
m, n = map(int, input().split(' '))
a = 1
for i in range(1, min(m, n)+1):
    if m % i == 0 and n % i == 0:
        a = i
print(int(m*n/a))
