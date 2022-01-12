"""
File: HJ2.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2022-01-13 00:48:38
Function:


"""

while True:
    try:
        string1 = input()
        alpha1 = input()
        string_after = string1.lower()
        alpha_after = alpha1.lower()
        print(string_after.count(alpha_after))
    except:
        break