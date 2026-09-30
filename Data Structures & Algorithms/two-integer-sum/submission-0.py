class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumHash = {}
        for i, n in enumerate(nums):
            if target-n in sumHash:
                return [sumHash[target-n], i]
            sumHash[n] = i
        return []