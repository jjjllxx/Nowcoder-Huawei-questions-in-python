"""
File: HJ13.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2022-01-13 00:55:22
Function:


"""

while True:
    try:
        str0 = input().split()
        for i in str0[::-1]:
            print(i, end=(' '))

    except:
        break