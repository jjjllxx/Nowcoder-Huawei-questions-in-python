def apple0(apple, plate):
    if apple < 0 or plate < 0:
        return 0
    elif apple == 1 or plate == 1:
        return 1
    else:
        return apple0(apple, plate - 1) + apple0(apple - plate, plate)

while True:
    try:
        m, n = map(int, input().split())
        print(apple0(m, n))
    except:
        break
