"""
File: HJ31.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2022-01-13 01:10:21
Function:


"""

while True:
    try:
        string0 = input()
        word0 = ''
        for i in string0:
            if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
                word0 += i
            else:
                word0 += ' '
        word_list = word0.split()
        for item in word_list[::-1]:
            print(item, end=' ')
    except:
        break
