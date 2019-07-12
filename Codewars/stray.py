def stray(arr):
    arr_1 = []
    arr_2 = []
    n = 0
    while n < len(arr) - 1:
        for el in arr:
            arr_1.append(el) if el == arr[n+1] else arr_2.append(el)
            n += 1
    return arr_1[0] if len(arr_1) == 1
    if len(arr_1) == 1:
        return arr_1[0]
    else:
        return arr_2[0]

print(stray([1, 1, 1, 1, 1, 1, 2]))