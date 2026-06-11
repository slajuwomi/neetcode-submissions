class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        R = 1

        for i in range(len(s) - 1):
            res += abs(ord(s[i]) - ord(s[R]))
            R += 1
        return res