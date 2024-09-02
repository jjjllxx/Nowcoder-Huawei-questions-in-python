while True:
    string = input()
    num = 0
    for i in string:
        if 65 <= ord(i) <= 90:
            num += 1
    print(num)
