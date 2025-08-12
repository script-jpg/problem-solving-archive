from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    candidates = sorted(candidates)

    def dfs(start, remaining):
        if remaining == 0:
            return [[]]
        else:
            res = []
            for i in range(start, len(candidates)):
                c = candidates[i]
                if c > remaining:
                    break
                for rest in dfs(i, remaining - c):
                    res.append([c] + rest)
            return res

    return dfs(0, target)
