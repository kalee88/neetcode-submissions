class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaGroups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            anaGroups[key].append(s)
        return list(anaGroups.values())
