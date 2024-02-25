# https://leetcode.com/problems/regular-expression-matching/
from functools import cache


class Solution:
    @cache
    def check(self, s, p):
        if len(p) == 0:
            return len(s) == 0
        if len(s) == 0:
            return len(p) > 1 and p[-1] == "*" and self.check(s, p[:-2])

        if p[-1] == "*":
            return self.check(s, p[:-2]) or ((p[-2] == s[-1] or p[-2] == ".") and self.check(s[:-1], p))
        return (p[-1] == '.' or s[-1] == p[-1]) and self.check(s[:-1], p[:-1])

    def isMatch(self, s: str, p: str) -> bool:
        return self.check(s, p)


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("ab", ".*"))
