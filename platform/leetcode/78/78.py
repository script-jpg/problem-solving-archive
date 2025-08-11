from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    def dfs(i, k, res, remaining, curr):
        if i == k:
            res.append(curr[:])
        else:
            dfs(i+1, k, res, remaining, curr)
            first = remaining[i]
            curr.append(first)
            dfs(i+1, k, res, remaining, curr)
            curr.pop()
    res = []
    dfs(0, len(nums), res, nums, curr = [])
    return res

if __name__ == '__main__':
    print(subsets([1,2]))
