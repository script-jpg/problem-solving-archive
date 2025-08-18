from collections import Counter
# checkInclusion a bit faster at O(m+n) compared to checkInclusion_(m*n)


def checkInclusion(s1: str, s2: str) -> bool:
    if len(s2) < len(s1):
        return False
    s1_counter = [0] * 26
    for c in s1:
        s1_counter[ord(c) - ord("a")] += 1

    s2_counter = [0] * 26
    i = 0
    for j in range(len(s2)):
        s2_counter[ord(s2[j]) - ord("a")] += 1
        if (j - i + 1) > len(s1):
            s2_counter[ord(s2[i]) - ord("a")] -= 1
            i += 1
        if s1_counter == s2_counter:
            return True
    return False


def checkInclusion_(s1: str, s2: str) -> bool:
    if len(s2) < len(s1):
        return False
    s1_counter = Counter(s1)
    return any(Counter(s2[i : i + len(s1)]) == s1_counter for i in range(len(s2)))
