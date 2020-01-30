from bisect import bisect


def lnd_seq(lst):
    n = len(lst)

    d = [-1] + [10**10 for _ in range(n)]
    pos = [-1] + [10**10 for _ in range(n)]
    prev = [0 for _ in range(n)]
    length = 0

    for i in range(n):
        j = bisect(d, lst[i])
        if d[j - 1] <= lst[i] < d[j]:
            d[j] = lst[i]
            pos[j] = i
            prev[i] = pos[j - 1]
            length = max(length, j)

    res = []
    pointer = pos[length]

    while pointer != -1:
        res.append(lst[pointer])
        pointer = prev[pointer]

    print(length)
    print(*reversed(res))


def main():
    a = [int(element) for element in input().split()]

    lnd_seq(a)


if __name__ == '__main__':
    main()
