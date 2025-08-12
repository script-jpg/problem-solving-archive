from typing import List
from collections import defaultdict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    def encode(s: str) -> List[int]:
        encoding = [0] * 26
        for c in s:
            encoding[ord(c) - ord("a")] += 1
        return encoding

    d = defaultdict(list)
    for s in strs:
        counter = encode(s)
        d[tuple(counter)].append(s)
    return list(d.values())


if __name__ == "__main__":
    print(
        """groupAnagrams(["eat","tea","tan","ate","nat","bat"]) = """,
        groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
    )
