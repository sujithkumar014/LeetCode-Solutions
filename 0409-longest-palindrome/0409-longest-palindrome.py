class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}

        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        ans = 0
        odd = False

        for x in d.values():
            ans += (x // 2) * 2

            if x % 2 == 1:
                odd = True

        if odd:
            ans += 1

        return ans