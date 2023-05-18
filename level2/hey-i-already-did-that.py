def to_base_b(str_base_10, base): #This function returns a string
    if str_base_10 == '0':
        return '0'

    rem, base_b = int(str_base_10), ''

    while rem:
        base_b = str(int(rem % base)) + base_b
        rem //= base

    return base_b

def to_base_10(str_base_b, base): #This function returns a string
    if str_base_b == '0':
        return '0'

    n, base_10 = len(str_base_b), 0

    for i, digit in enumerate(str_base_b):
        base_10 += int(digit) * pow(base, (n-i-1))

    return str(base_10)


def solution(n, b):
    # 1. identify k and list of ids
    k = len(n)
    id_log = []

    # v will be the iteratively decreasing value derived from n
    v = n

    while v not in id_log and v != 0:
        id_log.append(v)

        # 2. Find x and y
        y = ''.join(sorted(v))
        x = y[::-1]

        if b == 10:
            # 3. Find z as int and convert to string (with leading zeros if needed)
            z = str(int(x) - int(y))

            v = z if len(z) == k else (k - len(z)) * '0' + z
        else:
            # 4. If not base 10, convert x and y to base 10 to find z in base 10
            z_base_10 = int(to_base_10(x,b)) - int(to_base_10(y,b))

            # 5. Convert z_base_10 back to base b
            z = to_base_b(z_base_10,b)

            # 6. Add leading zeros if necessary
            v = z if len(z) == k else (k - len(z)) * '0' + z

    return len(id_log) - id_log.index(v)
