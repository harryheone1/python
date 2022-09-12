# noinspection DuplicatedCode
def swap_binary_neighbor(arr):
    l = l_tar = 0
    r = r_tar = len(arr) - 1
    l_res = r_res = 0
    while l < len(arr) and r >= 0:
        if arr[l] == 1:
            l_res += l - l_tar
            l_tar += 1
        if arr[r] == 1:
            r_res += r_tar - r
            r_tar -= 1
        l += 1
        r -= 1

    return min(l_res, r_res)


def main():
    tests = list()

    test1 = [0, 1, 0, 1]
    test2 = [1, 0, 1, 0]
    test3 = [1, 0, 1, 0, 0, 0, 0, 1]
    test4 = [1, 0, 0, 0, 0, 1, 0, 1]

    tests.append(test1)
    tests.append(test2)
    tests.append(test3)
    tests.append(test4)
    tests.append(list())

    for test in tests:
        print("------------")
        print(test)
        print(swap_binary_neighbor(test))
        print("------------")


main()
