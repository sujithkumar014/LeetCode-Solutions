class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()

        result = []

        for i in intervals:
            if not result or result[-1][1] < i[0]:
                result.append(i)
            else:
                result[-1][1] = max(result[-1][1], i[1])

        return result