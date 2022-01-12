"""
File: HJ7.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2022-01-13 00:54:19
Function:


"""

while True:
    try:
        a=float(input())
        if a-int(a) >= 0.5:
            print(int(a)+1)
        else:
            print(int(a))
    except:
        break