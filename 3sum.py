# https://leetcode.com/problems/3sum/description/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        in_list = {}

        for num in nums:
            in_list[num] = in_list.get(num, 0) + 1

        res = set()

        for i in in_list.keys():
            for j in in_list.keys():
                if in_list.get(-(i + j), False):
                    ans = [i, j, -(i + j)]

                    for elem in ans:
                        if ans.count(elem) > in_list[elem]:
                            break
                    else:
                        res.add(tuple(sorted(ans)))

        return list(map(list, list(res)))


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum([0, 1, 1]))
    print(s.threeSum([0, 0, 0]))
