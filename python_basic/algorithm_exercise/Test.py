"""
merge process:
1) use Email as key, O(1) to find if there is already same Email existing. (A Hashmap: Email -> Person(Group))
2) If yes, O(1) to merge two different people's Email to same group.(A Hashmap: Person -> Email)
3) If there are multiple group should be merged, merge them one by one. (Modify two hashmaps)
4) Print out the list of Email by the Hashmap of : Person -> Email
"""
# merge process
from collections import defaultdict
from typing import List


class Answer:

    def b_search_circular(nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if target > nums[mid]:
                if target < nums[end]:  # 4561234
                    start = mid + 1
                elif target > nums[end]:  #
                    end = mid - 1
                else:
                    return end

            elif target < nums[mid]:
                if target > nums[start]:
                    end = mid - 1
                elif target < nums[start]:
                    start = mid + 1
                else:
                    return start
            else:
                return mid
