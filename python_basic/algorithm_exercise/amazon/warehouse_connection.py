def number_of_warehouse(level):
    count = 0
    for cel in level:
        if cel == 1:
            count += 1
    return count


def number_of_connections(graph):
    pre_lvl = 0
    res = 0

    for level in graph:
        # if pre_lvl == -1:
        #     pre_lvl = number_of_warehouse(level)
        # else:
        warehouse_count = number_of_warehouse(level)
        if warehouse_count > 0:
            res += pre_lvl * warehouse_count
            pre_lvl = warehouse_count

    return res


def main():
    tests = list()

    test1 = [[1, 1, 1], [0, 1, 0], [0, 0, 0], [1, 1, 0]]
    test2 = [[0, 0, 0], [0, 1, 0], [1, 1, 1], [1, 1, 0]]

    tests.append(test1)
    tests.append(test2)
    tests.append(list())

    for test in tests:
        print("------------")
        print(test)
        print(number_of_connections(test))
        print("------------")


main()
