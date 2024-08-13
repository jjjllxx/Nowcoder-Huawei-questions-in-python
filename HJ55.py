num = int(input())
n = 0
for i in range(1, num+1):
    if i % 7 == 0 or '7' in str(i):
        n += 1
print(n)
