"""
File: HJ38.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2022-01-13 01:10:58
Function:


"""
while True:
    try:
        distance = int(input())
        distance_all = 0
        for i in range(5):
            distance_all += distance
            distance = distance / 2
            distance_all += distance
        print(distance_all - distance)
        print(distance)
    except:
        break
