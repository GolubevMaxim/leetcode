# https://leetcode.com/problems/longest-palindromic-substring/
from functools import cache


class Solution:
    def is_palindrome(self, s: str):
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                if self.is_palindrome(s[j:j + i]):
                    return s[j:j + i]


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('babad'))
