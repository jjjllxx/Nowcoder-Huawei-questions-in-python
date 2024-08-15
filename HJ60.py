def judgePrimeNumber(n):
    m = 0
    for item in range(2, int(n ** 0.5) + 1):
        if n % item == 0:
            return 0
    return 1

while True:
    try:
        num = int(input())
        a, b = 0, 0
        for i in range(1, int(num / 2)+1, 2):
            if judgePrimeNumber(i) and judgePrimeNumber(num - i):
                a = i
                b = num - i
        print(a, b, end='\n')
    except:
        break
