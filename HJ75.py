"""
File: HJ75.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2021-07-29 17:04:17
Function:


"""
string1 = input()
string2 = input()
num, num_max = 0, 0
for i in range(len(string1)):
    location = string2.find(string1[i])
    if location != -1:
        for j in range(location, min(len(string2), location+len(string1)-i)):
            if string2[j] == string1[i+j-location]:
                num += 1
            else:
                break
        if num > num_max:
            num_max = num
    num = 0
print(num_max)
