"""
File: HJ76.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2021-07-28 16:20:21
Function:


"""
num = int(input())
string = ''
if num <= 100:
    for i in range(num):
        a = num ** 2 - num + 1 + 2 * i
        string += str(a)
        string += '+'
print(string[:len(string) - 1:])
