def lms(lst):
    n = len(lst)
    temp = [1 for i in range(n)]

    for i in range(n):
        for j in range(i):
            if lst[i] % lst[j] == 0 and temp[j] + 1 > temp[i]:
                temp[i] = temp[j] + 1

    res = max(0, *temp)

    return res


def main():
    n = int(input())
    a = [int(element) for element in input().split()]
    print(lms(a))


if __name__ == '__main__':
    main()
