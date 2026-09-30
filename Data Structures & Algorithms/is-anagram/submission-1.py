class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        for n in s:
            counts[n] = counts.get(n,0) + 1
        for n in t:
            if n not in counts or counts[n] == 0:
                return False
            counts[n] -= 1
        return True