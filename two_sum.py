from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        sorted_nums = sorted(nums)

        while left < right:
            s = sorted_nums[left] + sorted_nums[right]
            if s == target:
                res1 = nums.index(sorted_nums[left])
                res2 = nums.index(sorted_nums[right], res1 + 1 if sorted_nums[left] == sorted_nums[right] else 0)
                return [res1, res2]
            if s < target:
                left += 1
            if s > target:
                right -= 1
