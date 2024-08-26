while True:
    try:
        n = int(input())
        dict0={}
        for i in range(n):
            line0 = input().split()
            key0 = int(line0[0])
            value0 = int(line0[1])
            if key0 not in dict0.keys():
                dict0[key0] = value0
            else:
                dict0[key0] += value0
        for key1 in sorted(dict0.keys()):
            print(key1, end = ' ')
            print(dict0[key1])
    except:
        break
