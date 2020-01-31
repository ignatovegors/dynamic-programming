def lev_dist_matrix(a, b):
    table = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    for i in range(len(a) + 1):
        table[i][0] = i

    for j in range(1, len(b) + 1):
        table[0][j] = j

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                diff = 0
            else:
                diff = 1

            conf = table[i - 1][j - 1] + diff
            rem = table[i - 1][j] + 1
            ins = table[i][j - 1] + 1

            table[i][j] = min(conf, rem, ins)

    return table[-1][-1]


def main():
    a = str(input())
    b = str(input())

    print(lev_dist(a, b))


if __name__ == '__main__':
    main()
