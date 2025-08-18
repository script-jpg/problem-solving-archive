from typing import List
from collections import deque


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    nums_ = [(num, i) for i, num in enumerate(nums)]
    deq = deque()

    def append(deq, elem):
        while deq and deq[-1][0] < elem[0]:
            deq.pop()
        deq.append(elem)

    def go(j, res):
        if j == len(nums_):
            return res
        else:
            append(deq, nums_[j])
            if j >= k - 1:
                if j > k - 1 and deq[0][1] < j - k + 1:
                    deq.popleft()
                res.append(deq[0][0])
            return go(j + 1, res)

    return go(0, [])
