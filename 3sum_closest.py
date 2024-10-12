# https://leetcode.com/problems/3sum-closest/
from typing import List


class Solution:
    def twoSum(self, numbers, target, ind_exclude):
        left, right = ind_exclude + 1, len(numbers) - 1

        best = abs(target - (numbers[left] + numbers[right]))
        best_left, best_right = left, right
        while left < right:
            if numbers[left] + numbers[right] == target:
                return 0, left, right

            if best > abs(target - (numbers[left] + numbers[right])):
                best = abs(target - (numbers[left] + numbers[right]))
                best_left, best_right = left, right

            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

        return best, best_left, best_right

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        best = float('inf')
        best_left, best_right, best_i = -1, len(nums) - 1, 0

        for i in range(len(nums) - 2):
            res, left, right = self.twoSum(nums, target - nums[i], i)
            if res < best:
                best = res
                best_left, best_right, best_i = left, right, i

        return nums[best_i] + nums[best_right] + nums[best_left]


if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([-1, 0, 1, 2, -1, 4], 9))
    print(s.threeSumClosest([-1, 2, 1, 4], 1))
