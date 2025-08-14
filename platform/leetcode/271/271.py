from typing import List


def encode(strs: List[str]) -> str:
    """Encodes a list of strings to a single string."""
    return "".join(f"{len(s)}:{s}" for s in strs)


def decode(s: str) -> List[str]:
    """Decodes a single string to a list of strings."""
    res, i = [], 0
    while i < len(s):
        j = s.find(":", i)
        L = int(s[i:j])
        i = j + 1  # Move to word
        str = s[i : i + L]  # get word
        res.append(str)
        i += L  # move i to next number pos
    return res
