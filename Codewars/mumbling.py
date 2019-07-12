def accum(s):
    n = 0
    result = ''
    for i in s:
        result += i.upper() + i.lower() * n + '-'
        n += 1
    return result[:-1]

print(accum("ZpglnRxqenU"))  # "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"

