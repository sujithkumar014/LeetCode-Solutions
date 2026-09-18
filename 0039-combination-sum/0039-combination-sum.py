class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(start, current, total):
            if total == target:
                result.append(current.copy())
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])

                # i, not i+1 → same number can be used again
                backtrack(i, current, total + candidates[i])

                current.pop()

        backtrack(0, [], 0)
        return result
        