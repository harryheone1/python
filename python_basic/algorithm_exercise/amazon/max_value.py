def max_val_arr(arr):
    memo = set()

    for num in arr:
        memo.add(num)

    return len(memo)

def main():
    tests = list()

    test1 = [1, 2, 2, 4]
    test2 = [3, 2, 4, 1]
    test3 = [1, 1, 1, 1]
    test4 = [1, 3, 5, 7]

    tests.append(test1)
    tests.append(test2)
    tests.append(test3)
    tests.append(test4)
    tests.append(list())

    for test in tests:
        print("------------")
        print(test)
        print(max_val_arr(test))
        print("------------")


main()