def swap_binary_arr(arr):
    l, r = 0, len(arr) - 1
    res = 0
    while l < r:  # [0, 0, 1, 0, 1], l = 2, r = 3
        if arr[l] == 1 and arr[r] == 0:
            arr[l], arr[r] = arr[r], arr[l]
            res += 1
        else:
            if arr[l] == 0:
                l += 1
            if arr[r] == 1:
                r -= 1

    return arr, res


def main():
    tests = list()

    test1 = [0, 1, 0, 1, 0]
    test2 = [1, 0, 1, 0]
    test3 = [1, 0, 1, 0, 0, 0, 0, 1]
    test4 = [1, 0, 0, 0, 0, 1, 0, 1]
    test5 = [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0]

    tests.append(test1)
    tests.append(test2)
    tests.append(test3)
    tests.append(test4)
    tests.append(test5)
    tests.append(list())

    for test in tests:
        print("------------")
        print(test)
        print(swap_binary_arr(test))
        print("------------")


main()
