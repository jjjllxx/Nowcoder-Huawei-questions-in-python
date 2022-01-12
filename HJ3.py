"""
File: HJ3.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2022-01-13 00:53:20
Function:


"""

while True:
    try:
        num = int(input())
        num_list = []
        for i in range(num):
            a = int(input())
            if a not in num_list:
                num_list.append(a)
        num_list.sort()
        for item in num_list:
            print(item)
    except:
        break