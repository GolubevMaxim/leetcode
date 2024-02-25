# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        positive = x >= 0

        x_str = str(x)[0 if positive else 1:]
        x_reverse = int(x_str[::-1]) * (1 if positive else -1)

        if x_reverse < -2 ** 31 or x_reverse > 2 ** 31:
            return 0
        return x_reverse


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(0))
