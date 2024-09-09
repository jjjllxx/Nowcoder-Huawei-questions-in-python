string1 = input()
transfer = {'1': '1', 'abc': '2', 'def': '3', 'ghi': '4', 'jkl': '5', 'mno': '6', 'pqrs': '7', 'tuv': '8', 'wxyz': '9'}
string_after = ''
for i in string1:
    if i.islower():
        for item in transfer.keys():
            if i in item:
                string_after += transfer[item]
    elif i.isdigit():
        string_after += i
    elif i.isupper():
        if i == 'Z':
            string_after += 'A'
        else:
            string_after += chr(ord(i)+1)
print(string_after)
