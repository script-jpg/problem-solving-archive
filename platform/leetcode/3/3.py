from collections import defaultdict


def lengthOfLongestSubstring(s: str) -> int:
    best = 0
    d = defaultdict(int)
    i = 0
    for j in range(len(s)):
        d[s[j]] += 1
        while d[s[j]] > 1:
            d[s[i]] -= 1
            i += 1
        # now valid
        best = max(best, j - i + 1)
    return best
