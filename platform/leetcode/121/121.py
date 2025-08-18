from typing import List


def maxProfit(prices: List[int]) -> int:
    min_so_far, best = prices[0], 0
    for i in range(1, len(prices)):
        min_so_far = min(min_so_far, prices[i])
        best = max(best, prices[i] - min_so_far)
    return best
