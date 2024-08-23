num = int(input())
string = ''
if num <= 100:
    for i in range(num):
        a = num ** 2 - num + 1 + 2 * i
        string += str(a)
        string += '+'
print(string[:len(string) - 1:])
