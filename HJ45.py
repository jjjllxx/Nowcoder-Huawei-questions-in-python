n = int(input())
value_list = []
for i in range(n):
    beauty_value = 0
    count = {}
    string1 = input()
    for item in string1:
        if item not in count.keys():
            count[item] = string1.count(item)
    num = 26
    count_list = list(count.values())
    count_list.sort(reverse=True)
    for j in count_list:
        beauty_value += j * num
        num -= 1
    value_list.append(beauty_value)
for i in value_list:
    print(i)


