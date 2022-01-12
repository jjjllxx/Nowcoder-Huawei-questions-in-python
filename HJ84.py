"""
File: HJ84.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2021-07-29 00:49:21
Function:


"""
while True:
    string = input()
    num = 0
    for i in string:
        if 65 <= ord(i) <= 90:
            num += 1
    print(num)
