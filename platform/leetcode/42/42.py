from typing import List


def trap(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    res = 0
    max_l, max_r = 0, 0
    while l < r:
        max_l = max(max_l, height[l])
        max_r = max(max_r, height[r])
        if height[l] <= height[r]:
            res += min(max_l, max_r) - height[l]
            l += 1
        else:
            res += min(max_l, max_r) - height[r]
            r -= 1
    return res
