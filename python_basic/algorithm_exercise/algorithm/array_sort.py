import sys
from typing import List

compare_time_bubble = 0
move_time_bubble = 0
compare_time_insert = 0
move_time_insert = 0
compare_time_select = 0
move_time_select = 0
compare_time_merge = 0
move_time_merge = 0
compare_time_quick = 0
move_time_quick = 0

# time complexity = O(n*logn)
# space complexity = O(1)
# in_place = Yes
# keep order = Yes
# streaming = No
def quick_sort(nums: List[int]):
    def pivot_select(start, end):
        mid = int(start + (end - start) / 2)
        return (nums[start] + nums[mid] + nums[end]) / 3

    def quick_sort_re(start, end):
        global compare_time_quick, move_time_quick
        if start < end:
            pivot = pivot_select(start, end)
            lp = start
            for rp in range(start, end + 1):
                compare_time_quick += 1
                if nums[rp] < pivot:
                    compare_time_quick += 1
                    nums[lp], nums[rp] = nums[rp], nums[lp]
                    move_time_quick += 1
                    lp += 1

            quick_sort_re(start, lp - 1)
            quick_sort_re(lp, end)

        return

    quick_sort_re(0, len(nums) - 1)


# time complexity = O(n*logn)
# space complexity = O(n)
# in_place = No
# keep order = Yes
# streaming = Support, but time complexity become O(n^2) means O(n) for each new integer
def merge_sort(nums: List[int]) -> List[int]:
    def merge_sort_re(start, end):
        global compare_time_merge, move_time_merge
        if start < end:
            mid = int(start + (end - start) / 2)
            left_arr = merge_sort_re(start, mid)
            right_arr = merge_sort_re(mid + 1, end)
            res = []
            j = 0
            for i in range(len(left_arr)):
                left = left_arr[i]
                # if right finished first

                compare_time_merge += 1
                while j < len(right_arr) and left > right_arr[j]:
                    res.append(right_arr[j])
                    move_time_merge += 1
                    compare_time_merge += 1
                    j += 1
                res.append(left)
                move_time_merge += 1
            return res
        return [nums[start]]

    return merge_sort_re(0, len(nums) - 1)


# time complexity = O(n^2)
# space complexity = O(1)
# in_place = True
# keep order = Yes
# streaming = No
def bubble_sort(nums: List[int]):
    global compare_time_bubble, move_time_bubble
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            compare_time_bubble += 1
            if nums[j] > nums[j + 1]:
                move_time_bubble += 1
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return


# time complexity = O(n^2)
# space complexity = O(1)
# in_place = True
# keep order = Yes
# streaming = Yes
def insert_sort(nums: List[int]):
    global compare_time_insert, move_time_insert
    for i, num in enumerate(nums):
        # start, end = 0, i
        # TODO: binary search optimization
        loc = i
        for j in range(i):
            compare_time_insert += 1
            if nums[j] > num:
                loc = j
                break

        for k in range(i, loc, -1):
            move_time_insert += 1
            nums[k] = nums[k - 1]
        nums[loc] = num


# time complexity = O(n^2)
# space complexity = O(1)
# in_place = True
# keep order = Yes
# streaming = No
def select_sort(nums: List[int]):
    global compare_time_select, move_time_select
    for i in range(len(nums)):
        min_val = float('inf')
        min_idx = i
        for j in range(i, len(nums)):
            compare_time_select += 1
            if nums[j] < min_val:
                min_val = nums[j]
                min_idx = j

        move_time_select += 1
        nums[i], nums[min_idx] = nums[min_idx], nums[i]


def test_quick():
    input_ = [_ for _ in range(1000, 0, -1)]
    quick_sort(input_)
    print("Quick Sort result is: " + str(input_))
    # 1 + 2 + ... + 7 = (0 + 6) * 7 / 2 = 21
    print("Quick Sort compare and swap time: " + str(compare_time_quick) + " and " + str(move_time_quick))


def test_merge():
    input_ = [_ for _ in range(1000, 0, -1)]
    res = merge_sort(input_)
    # print("Merge Sort result is: " + str(res))
    # 1 + 2 + ... + 7 = (0 + 6) * 7 / 2 = 21
    print("Merge Sort compare and swap time: " + str(compare_time_merge) + " and " + str(move_time_merge))


def test_bubble():
    input_ = [_ for _ in range(1000, 0, -1)]
    bubble_sort(input_)
    # print("Bubble Sort result is: " + str(input_))
    # 1 + 2 + ... + 7 = (0 + 6) * 7 / 2 = 21
    print("Bubble Sort compare and swap time: " + str(compare_time_bubble) + " and " + str(move_time_bubble))


def test_insert():
    input_ = [_ for _ in range(1000, 0, -1)]
    insert_sort(input_)
    # print("Insert Sort result is: " + str(input_))
    # 1 + 2 + ... + 7 = (0 + 6) * 7 / 2 = 21
    print("Insert Sort compare and swap time: " + str(compare_time_insert) + " and " + str(move_time_insert))


def test_select():
    input_ = [_ for _ in range(1000, 0, -1)]
    select_sort(input_)
    # print("Select Sort result is: " + str(input_))
    # 1 + 2 + ... + 7 = (0 + 6) * 7 / 2 = 21
    print("Select Sort compare and swap time: " + str(compare_time_select) + " and " + str(move_time_select))


test_bubble()
test_insert()
test_select()
test_merge()
test_quick()
