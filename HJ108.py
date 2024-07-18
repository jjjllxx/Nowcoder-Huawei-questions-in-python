m, n = map(int, input().split(' '))
a = 1
for i in range(1, min(m, n)+1):
    if m % i == 0 and n % i == 0:
        a = i
print(int(m*n/a))
