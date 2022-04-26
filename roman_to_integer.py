'''
https://leetcode.com/problems/roman-to-integer/
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        result = 0

        prev_number = symbols[s[0]]
        accum = prev_number

        for letter in s[1:]:
            number = symbols[letter]
            if number == prev_number:
                accum += number
            if number > prev_number:
                result += number - accum
                accum = 0
            if number < prev_number:
                result += accum
                accum = number
            prev_number = number

        result += accum

        return result
