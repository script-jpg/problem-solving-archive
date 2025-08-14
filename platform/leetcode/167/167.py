from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    l, r = (0, len(numbers) - 1)
    inc = lambda x, y: [x + 1, y + 1]
    while l < r:
        sum = numbers[l] + numbers[r]
        if sum < target:
            l += 1
        elif sum > target:
            r -= 1
        else:
            return inc(l, r)
