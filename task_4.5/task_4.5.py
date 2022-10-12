# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Модуль сжатия данных:
def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data:
        return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


encoded_val = rle_encode('fffffffwqqqqqqd')
print(encoded_val)

# Модуль восстановления данных:


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


decoded_val = rle_decode('7f1w6q1d')
print(decoded_val)
