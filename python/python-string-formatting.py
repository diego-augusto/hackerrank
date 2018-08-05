def print_formatted(number):

    size = len(bin(number).replace('0b', ''))

    for i in range(1, number+1):

        v_oct = oct(i).replace('0o', '')
        v_hex = hex(i).replace('0x', '').upper()
        v_bin = bin(i).replace('0b', '')

        print(str(i).rjust(size), v_oct.rjust(size),
              v_hex.rjust(size), v_bin.rjust(size))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
