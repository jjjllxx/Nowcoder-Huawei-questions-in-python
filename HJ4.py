"""
File: HJ4.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2022-01-13 00:53:25
Function:


"""

while True:
    try:
        string1 = input()
        if len(string1)%8 != 0:
            string1 += (8-len(string1)%8) * '0'
        for i in range(len(string1)):
            if i%8 == 7:
                print(string1[i])
            else:
                print(string1[i],end='')
    except:
        break