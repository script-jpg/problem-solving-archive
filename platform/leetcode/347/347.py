from collections import Counter
from typing import List
import heapq


def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = Counter(nums)
    values = sorted(counter.items(), key = lambda x : x[1], reverse = True)
    res = map(lambda x: x[0], values[:k])
    return list(res)


def topKFrequent_(nums: List[int], k:int) -> List[int]:
    counter = Counter(nums)
    return [item for item, _ in heapq.nlargest(k, counter.items(), lambda x: x[1])]

if __name__ == "__main__":
    print(topKFrequent_([1,1,1,1,1,2,2,3], 2))
