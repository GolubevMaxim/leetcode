class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        used = dict()
        used[s[0]] = 0

        res = [0 for _ in s]
        res[0] = 1

        for ind, letter in enumerate(s[1:]):
            i = ind + 1
            if not (letter in used):
                res[i] = res[i - 1] + 1
            else:
                res[i] = min(i - used[letter], res[i - 1] + 1)
            used[letter] = i

        return max(res)


