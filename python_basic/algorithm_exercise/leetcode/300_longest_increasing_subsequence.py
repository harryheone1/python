import random
import timeit
from typing import List


def lengthOfLIS_labuladong(nums: List[int]):
    dp = list()
    for num in nums:
        cur = 0
        for idx in range(len(dp)):
            if nums[idx] < num:
                cur = max(dp[idx], cur)
        dp.append(cur + 1)

    return max(dp)


def lengthOfLIS_mine(nums):
    dp = list()
    dp.append(float('-inf'))
    for num in nums:  # 4 -> dp = [-inf, 4, 10]
        start, end = 0, len(dp) - 1
        # binary search
        idx_dp = -1
        while start <= end:  # 1, 1, 1
            mid = int(end / 2 + start / 2)
            if dp[mid] > num:
                if mid == start or dp[mid - 1] < num:
                    idx_dp = mid - 1
                    break
                end = mid - 1
            elif dp[mid] < num:
                if mid == end or dp[mid + 1] > num:
                    idx_dp = mid
                    break
                start = mid + 1
            else:
                break
        # idx_dp = 2
        if idx_dp == len(dp) - 1:
            dp.append(num)
        elif idx_dp >= 0:
            dp[idx_dp + 1] = num

    return len(dp) - 1


def main():
    tests = list()

    test1 = [10, 9, 2, 5, 3, 7, 101, 18]
    test2 = [0, 1, 0, 3, 2, 3]
    test3 = [7, 7, 7, 7, 7, 7, 7]
    test4 = []
    for i in range(0, 50000):
        n = random.randint(1, 1000000)
        test4.append(n)

    tests.append(test1)
    tests.append(test2)
    tests.append(test3)
    tests.append(test4)

    start = timeit.default_timer()
    for test in tests:
        #print("------------")
        #print(test)
        res = lengthOfLIS_labuladong(test)
        #print(res)
        #print("------------")
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    start = timeit.default_timer()
    for test in tests:
        #print("------------")
        #print(test)
        res = lengthOfLIS_mine(test)
        #print(res)
        #print("------------")
    stop = timeit.default_timer()
    print('Time: ', stop - start)


main()
