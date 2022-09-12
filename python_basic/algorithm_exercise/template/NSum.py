from typing import List


class NSum:
    def nSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)

        def nsum_dv(nums: List[int], target: int, n: int) -> List[List[int]]:
            res = set()
            m = len(nums)

            if n == 2:
                i, j = 0, len(nums) - 1
                while i < j:
                    if nums[i] + nums[j] < target:
                        i += 1
                    elif nums[i] + nums[j] > target:
                        j -= 1
                    else:
                        res.add((nums[i], nums[j]))
                        i += 1
                        j -= 1
                return res

            for i in range(m - n + 1):
                sub_ans = nsum_dv(nums[i + 1:], target - nums[i], n - 1)
                for t_an in sub_ans:
                    l_an = list(t_an)
                    l_an.append(nums[i])
                    res.add(tuple(l_an))

            return res

        res = nsum_dv(nums, target, 4)
        ans = []
        for tuple_re in res:
            ans.append(list(tuple_re))

        return ans