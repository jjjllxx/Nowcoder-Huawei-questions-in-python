while True:
    try:
        a=float(input())
        if a-int(a) >= 0.5:
            print(int(a)+1)
        else:
            print(int(a))
    except:
        break
