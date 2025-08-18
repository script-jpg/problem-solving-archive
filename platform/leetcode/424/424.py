from collections import defaultdict


def characterReplacement(self, s: str, k: int) -> int:
    best = 0
    i = 0
    d = defaultdict(int)
    maxCount = 0

    for j in range(len(s)):
        d[s[j]] += 1
        maxCount = max(d[s[j]], maxCount)
        while maxCount + k < (j - i + 1):
            d[s[i]] -= 1
            i += 1
        best = max(best, j - i + 1)
    return best
