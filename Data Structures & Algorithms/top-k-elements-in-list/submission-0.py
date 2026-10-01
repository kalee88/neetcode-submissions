class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        for n in nums:
            hashMap[n] += 1
        key_list = []
        for n in range(k):
            max_key = max(hashMap, key=lambda k: hashMap[k])
            hashMap.pop(max_key)
            key_list.append(max_key)
        return key_list
    