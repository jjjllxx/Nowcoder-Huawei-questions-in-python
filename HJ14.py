"""
File: HJ14.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2022-01-13 00:55:29
Function:


"""
while True:
    try:
        num = int(input())
        list0 = {}
        for i in range(num):
            word_new = input()
            if word_new in list0.keys():
                list0[word_new] += 1
            else:
                list0[word_new] = 1
        for item0 in sorted(list0):
            for i in range(list0[item0]):
                print(item0)
    except:
        break