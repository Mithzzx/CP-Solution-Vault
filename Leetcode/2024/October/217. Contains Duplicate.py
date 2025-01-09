from collections import Counter


def isAngaram(s: str, t: str) -> bool:
    if Counter(s) == Counter(t):
        return True
    return False
