"""
File: HJ107.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2022-01-13 01:07:19
Function:


"""

while True:
    try:
        num = float(input())
        if num >= 0:
            print(format(num**(1/3),'.1f'))
        else:
            print(format(0-abs(num**(1/3)),'.1f'))
    except:
        break