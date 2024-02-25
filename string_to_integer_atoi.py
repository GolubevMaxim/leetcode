# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        positive = s[0] != '-'

        if s[0] in "+-":
            s = s[1:]

        i = 0
        while i < len(s) and s[i] in "0123456789":
            i += 1

        if s[:i] == '':
            return 0

        x = int(s[:i]) * (1 if positive else -1)

        if x > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if x < -2 ** 31:
            return -2 ** 31
        return x


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("words and 987"))
