m_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
y, m, d = map(int, input().split(' '))
num = 0
for i in range(m-1):
    num += m_length[i]
num += d
if ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0) and m >= 3:
    num += 1
print(num)
