def base_convert(num: int, base: int) -> int:
    if num == 0:
        return [0]

    if 2 > base < 9:
        raise ValueError('La base doit etre entre 2 et 9')

    result: list[int] = []

    while num > 0:
        result.append(num % base)
        num = num // base

    return result


def read_base_convert(num: int, base: int) -> int:
    result = base_convert(num, base)
    value = ''

    for digit in result:
        value = str(digit) + value

    return int(value)


if __name__ == '__main__':
    for num in range(1000):
        assert read_base_convert(num, 2) == int(bin(num).removeprefix('0b'))

    print(base_convert(0, 2))
