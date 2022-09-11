from tokenize import Number


def pat16(n: int):
    coef = 1
    for row in range(1, n + 1):
        print("  " * (n - row), end="")
        for col in range(0, row):
            if col == 0 or row == 0:
                coef = 1
            else:
                coef = coef * (row - col) // col
            print("  ", coef, end="")
        print()


pat16(int(6))
