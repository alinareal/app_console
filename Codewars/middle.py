def get_middle(s):
    middle = len(s) / 2
    if len(s) % 2 == 1:
        return s[middle]
    else:
        return s[middle - 1:middle + 1]
