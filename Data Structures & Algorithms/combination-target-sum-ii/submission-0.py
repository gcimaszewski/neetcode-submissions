class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        solution = []
        summands = []

        candidates.sort()

        def backtrack(idx, dist):
            # to make sure no elements from `candidates` are used twice:
            # use an index to keep track of list of eligible nums for backtracking

            if dist == 0:
                solution.append(summands[:])
                return
            
            for j in range(idx, len(candidates)):
                n = candidates[j]
                if j > idx and candidates[j] == candidates[j-1]:
                    continue
                if dist - n >= 0:
                    summands.append(n)
                    backtrack(j + 1, dist - n)
                    summands.pop()

        backtrack(0, target)
        return solution