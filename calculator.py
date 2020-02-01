def calc(n):
    if n == 1:
        return [1]

    counter = 1

    dic = {n: [-1, 0]}

    prev = {n}
    pres = set()

    while True:
        for element in prev:
            if element % 2 == 0:
                pres.add(element // 2)
                if (element // 2 in dic and dic[element // 2][1] > counter) or element // 2 not in dic:
                    dic[element // 2] = [element, counter]
            if element % 3 == 0:
                pres.add(element // 3)
                if (element // 3 in dic and dic[element // 3][1] > counter) or element // 3 not in dic:
                    dic[element // 3] = [element, counter]
            pres.add(element - 1)
            if (element - 1 in dic and dic[element - 1][1] > counter) or element - 1 not in dic:
                dic[element - 1] = [element, counter]

        if 1 in pres:
            break

        prev = pres
        pres = set()
        counter += 1

    pointer = dic[1][0]
    res = [1, pointer]

    while pointer != -1:
        res.append(dic[pointer][0])
        pointer = dic[pointer][0]

    return res[:-1:]


def main():
    n = int(input())

    a = calc(n)

    print(len(a) - 1)
    print(*a)


if __name__ == '__main__':
    main()
