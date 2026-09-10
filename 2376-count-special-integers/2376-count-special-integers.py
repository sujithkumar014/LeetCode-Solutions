class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        ans = 0

        # Count numbers with fewer digits
        for length in range(1, len(s)):
            ans += 9 * self.permute(9, length - 1)

        # Count numbers with same number of digits
        used = set()

        for i, ch in enumerate(s):
            d = int(ch)

            start = 1 if i == 0 else 0

            for x in range(start, d):
                if x not in used:
                    ans += self.permute(10 - i - 1, len(s) - i - 1)

            if d in used:
                break

            used.add(d)
        else:
            ans += 1

        return ans

    def permute(self, n, r):
        result = 1
        for i in range(r):
            result *= n - i
        return result