while True:
    try:
        num = float(input())
        if num >= 0:
            print(format(num**(1/3),'.1f'))
        else:
            print(format(0-abs(num**(1/3)),'.1f'))
    except:
        break
