def stairs(n, steps):
    dic = {0: 0}
    prev = {0: 0}
    pres = {}
    flag = 0

    while True:
        flag = 0
        for element in prev:
            if element + 1 <= n:
                flag = 1
                if (element + 1 in pres and pres[element + 1] < prev[element] + steps[element + 1]) or element + 1 not\
                        in pres:
                    pres[element + 1] = prev[element] + steps[element + 1]
                    if (element + 1 in dic and dic[element + 1] < pres[element + 1]) or element + 1 not in dic:
                        dic[element + 1] = pres[element + 1]
            if element + 2 <= n:
                flag = 1
                if (element + 2 in pres and pres[element + 2] < prev[element] + steps[element + 2]) or element + 2 not\
                        in pres:
                    pres[element + 2] = prev[element] + steps[element + 2]
                    if (element + 2 in dic and dic[element + 2] < pres[element + 2]) or element + 2 not in dic:
                        dic[element + 2] = pres[element + 2]
        prev = pres
        pres = {}

        if not flag:
            break

    return dic[n]


def main():
    n = int(input())
    steps = [0] + [int(element) for element in input().split()]

    print(stairs(n, steps))


if __name__ == '__main__':
    main()
