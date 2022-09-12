class Solution:
    def findDuplicate(self, nums):
        # for i, num in enumerate(nums):
        #     while num != i + 1:
        #         if num[num - 1] == num[i]:
        #             return num[i]
        #         num[i], num[num[i] - 1] = num[num[i] - 1], num[i]
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[nums[i] - 1] == nums[i]:
                    return nums[i]
                nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]

        return None

so = Solution()
so.findDuplicate([1, 3, 4, 2, 2])