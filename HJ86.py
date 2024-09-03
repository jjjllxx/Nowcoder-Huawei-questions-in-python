while True:
    n = str(bin(int(input())))
    num, num_max = 0, 0
    for i in n:
        if i == '1':
            num += 1
            if num > num_max:
                num_max = num
        else:
            num = 0
    print(num_max)
