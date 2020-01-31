def lev_dist(a, b):
    if len(b) > len(a):
        temp = a
        a = b
        b = temp

    i = 1
    prev = [j for j in range(len(b) + 1)]

    while i < len(a) + 1:
        pres = [i]
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                diff = 0
            else:
                diff = 1

            conf = prev[j - 1] + diff
            rem = prev[j] + 1
            ins = pres[j - 1] + 1

            pres.append(min(conf, rem, ins))

        i += 1
        prev = pres

    return prev[-1]


def main():
    a = str(input())
    b = str(input())

    print(lev_dist(a, b))


if __name__ == '__main__':
    main()
