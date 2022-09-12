def invest_max_val(n, rounds):
    invests = [0] * n

    for r in rounds:
        l, r, val = r[0] - 1, r[1] - 1, r[2]
        invests[l] += val
        if r < n - 1:
            invests[r + 1] -= val

    amount = 0
    res = 0
    for invest in invests:
        amount += invest
        res = max(amount, res)

    return res

def main():
    tests = list()

    test1 = [5, [[1, 2, 10], [2, 4, 5], [3, 5, 12]]]

    tests.append(test1)

    for test in tests:
        print("------------")
        print(test)
        print(invest_max_val(test[0], test[1]))
        print("------------")


main()