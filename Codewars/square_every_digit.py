def square_digits(num):
    num_list = []
    for num in list(str(num)):
        num_list.append(str(int(num) ** 2))
    return int(''.join(num_list))

print(square_digits(1234))


def find_short(s):
    word_list = s.split()
    len_list = []
    for word in word_list:
        len_list.append(len(word))
    return min(len_list)

print(find_short('bitcoin take over the world maybe who knows perhaps'))
