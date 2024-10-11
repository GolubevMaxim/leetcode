# https://leetcode.com/problems/longest-common-prefix/description/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        flag = 1

        i = 0
        max_i = len(min(strs, key=len))

        while flag and i < max_i:
            for s in strs:
                if strs[0][i] != s[i]:
                    flag = 0

            i += 1

        if flag:
            return strs[0][:i]
        return strs[0][:i - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
