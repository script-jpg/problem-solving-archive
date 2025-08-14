from typing import List

def longestConsecutive(nums: List[int]) -> int:
    num_set = set(nums)
    best = 0
    for num in num_set:
        if num - 1 not in num_set:
            count = 1
            next = num + 1
            while next in num_set:
                count += 1
                next += 1
            best = max(best, count)
    return best
