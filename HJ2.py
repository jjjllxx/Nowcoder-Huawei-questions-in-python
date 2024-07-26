while True:
    try:
        string1 = input()
        alpha1 = input()
        string_after = string1.lower()
        alpha_after = alpha1.lower()
        print(string_after.count(alpha_after))
    except:
        break
