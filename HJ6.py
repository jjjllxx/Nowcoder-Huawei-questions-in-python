"""
File: HJ6.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2022-01-13 00:54:12
Function:


"""

while True:
    try:
        num = int(input())
        i = 2
        while num > 1:
            for j in range(2, int(num ** 0.5) + 2):
                if num % j == 0:
                    break
            if j == int(num ** 0.5) + 1:
                print(num)
                break
            if num % i == 0:
                print(i, end=(' '))
                num = int(num / i)
            else:
                i += 1

    except:
        break

# out of time, take care of big factor number
# while True:
#     try:
#         num = int(input())
#         i = 2
#         while num > 1:
#             if num % i == 0:
#                 print(i, end=(' '))
#                 num = int(num / i)
#             else:
#                 if i == 2:
#                     i += 1
#                 else:
#                     i += 2
#     except:
#         break

