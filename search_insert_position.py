from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while right - left > 1:
            center = (right + left) // 2
            if nums[center] > target:
                right = center
            elif nums[center] < target:
                left = center
            else:
                return center

        return right if nums[left] < target else left

