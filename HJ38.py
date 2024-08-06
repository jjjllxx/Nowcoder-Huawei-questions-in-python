while True:
    try:
        distance = int(input())
        distance_all = 0
        for i in range(5):
            distance_all += distance
            distance = distance / 2
            distance_all += distance
        print(distance_all - distance)
        print(distance)
    except:
        break
