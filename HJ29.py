"""
File: HJ29.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2022-01-13 01:09:03
Function:


"""


def coding(str_to_code):
    str_after_coding = ''
    for i in str_to_code:
        if i == '9':
            str_after_coding += '0'
        elif i == 'Z':
            str_after_coding += 'a'
        elif i == 'z':
            str_after_coding += 'A'
        elif i.isdigit():
            str_after_coding += chr(ord(i) + 1)
        elif i.islower():
            str_after_coding += chr(ord(i) - 31)
        elif i.isupper():
            str_after_coding += chr(ord(i) + 33)
    print(str_after_coding)


def decoding(str_to_decode):
    str_after_decoding = ''
    for i in str_to_decode:
        if i == '0':
            str_after_decoding += '9'
        elif i == 'a':
            str_after_decoding += 'Z'
        elif i == 'A':
            str_after_decoding += 'z'
        elif i.isdigit():
            str_after_decoding += chr(ord(i) - 1)
        elif i.islower():
            str_after_decoding += chr(ord(i) - 33)
        elif i.isupper():
            str_after_decoding += chr(ord(i) + 31)
    print(str_after_decoding)


while True:
    try:
        str1 = input()
        str2 = input()
        coding(str1)
        decoding(str2)
    except:
        break
