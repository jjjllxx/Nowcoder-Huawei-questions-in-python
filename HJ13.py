while True:
    try:
        str0 = input().split()
        for i in str0[::-1]:
            print(i, end=(' '))

    except:
        break
