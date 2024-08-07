while True:
    try:
        string1 = input()
        if len(string1)%8 != 0:
            string1 += (8-len(string1)%8) * '0'
        for i in range(len(string1)):
            if i%8 == 7:
                print(string1[i])
            else:
                print(string1[i],end='')
    except:
        break
