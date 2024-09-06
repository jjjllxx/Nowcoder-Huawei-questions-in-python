n = int(input())
num = 0
for i in range(n + 1):
    if i == i ** 2 % (10**len(str(i))):
        num += 1
print(num)
