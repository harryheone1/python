def len_of_substring(s):
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

    test1 = 'bbbbbaaaab'
    test2 = 'bbbbccdded'

    tests.append(test1)
    tests.append(test2)
    tests.append(list())

    for test in tests:
        print("------------")
        print(test)
        print(number_of_connections(test))
        print("------------")


main()