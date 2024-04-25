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
    

def print_base_convert(num: int, base: int) -> None:
    result = base_convert(num, base)

    for digit in result[::-1]:
        print(digit)


if __name__ == '__main__':
    num = int(input('Entrez un nombre en base 10 a convertir: '))
    base = int(input('Entrer la base vers laquelle convertir: '))

    print_base_convert(num, base)
