# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        merged_arr = []

        ind1, ind2 = 0, 0
        while ind1 < len(nums1) and ind2 < len(nums2) and len(merged_arr) < total_length // 2 + 1:
            if nums1[ind1] < nums2[ind2]:
                merged_arr.append(nums1[ind1])
                ind1 += 1
            else:
                merged_arr.append(nums2[ind2])
                ind2 += 1

        while ind1 < len(nums1) and len(merged_arr) < total_length // 2 + 1:
            merged_arr.append(nums1[ind1])
            ind1 += 1

        while ind2 < len(nums2) and len(merged_arr) < total_length // 2 + 1:
            merged_arr.append(nums2[ind2])
            ind2 += 1

        if total_length % 2 == 0:
            return (merged_arr[-1] + merged_arr[-2]) / 2
        return merged_arr[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1, 2], [3, 4]))
