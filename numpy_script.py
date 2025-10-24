import numpy as np


def _1d_array():
    a = np.array([1, 2, 3, 4, 5, 6])
    print(f"a: {a}")
    print()


def _3d_array():
    c = np.array([
        [[1, 2, 3], [3, 4, 5]],
        [[6, 7, 8], [9, 10, 11]]
    ])

    print(f"c: {c}")
    print(f"c[1][0][2]: {c[1][0][2]}")  # 8
    print()


def main():
    _1d_array()
    _3d_array()


if __name__ == '__main__':
    main()
