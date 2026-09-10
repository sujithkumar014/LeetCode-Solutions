class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        b = []
        count = {}
        ans = 0

        for i in range(len(arrivals)):
            # Remove items outside the last w days
            while b and b[0][0] <= i - w:
                day, item = b.pop(0)
                count[item] -= 1

            item = arrivals[i]

            if count.get(item, 0) >= m:
                ans += 1
            else:
                b.append((i, item))
                count[item] = count.get(item, 0) + 1

        return ans