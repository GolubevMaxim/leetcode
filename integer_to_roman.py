# https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        res = []

        roman_def = "IXCM"
        roman_fiv = "VLD"

        for p, d in enumerate(reversed(str(num))):
            if d == '0':
                continue

            d = int(d)
            if d == 4:
                res.append(roman_fiv[p])
                res.append(roman_def[p])
            elif d == 9:
                res.append(roman_def[p + 1])
                res.append(roman_def[p])
            elif d > 4:
                res += [roman_def[p] * (d - 5)]
                res.append(roman_fiv[p])
            else:
                res += [roman_def[p] * d]

        return ''.join(res[::-1])


if __name__ == '__main__':
    solution = Solution()
    print(solution.intToRoman(1994))
