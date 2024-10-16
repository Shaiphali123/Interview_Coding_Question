def print_formatted(number):
    for i in range(1, number + 1):
        dec = str(i)
        Oct = str(oct(i))[2:]
        Hex = str(hex(i))[2:].upper()
        Binary = str(bin(i))[2:]

        print(f"{dec:>5} {Oct:>5} {Hex:>5} {Binary:>8}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)