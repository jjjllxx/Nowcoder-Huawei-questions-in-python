month = int(input())
num = [1, 1]
for i in range(2, month):
    num.append(num[i-2]+num[i-1])
print(num[month-1])
