# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        lines = [[] for _ in range(numRows)]

        up = True
        level = 0
        for char in s:
            lines[level].append(char)

            level += 1 if up else -1
            if level == numRows - 1:
                up = False

            if level == 0:
                up = True

        return ''.join([''.join(line) for line in lines])


if __name__ == '__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING", 1))
