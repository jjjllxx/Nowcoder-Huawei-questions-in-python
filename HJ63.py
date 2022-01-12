"""
File: HJ63.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2021-07-30 22:58:25
Function:


"""
string1 = input()
length = int(input())
string_list = []
rate = 0
for i in range(len(string1)-length):
    if (string1[i:i + length:].count('C') + string1[i:i + length:].count('G'))/length > rate:
        rate = (string1[i:i + length:].count('C') + string1[i:i + length:].count('G'))/length
        string_list.append(string1[i:i + length:])
if len(string_list) == 0:
    print(string1)
else:
    print(string_list[len(string_list)-1])