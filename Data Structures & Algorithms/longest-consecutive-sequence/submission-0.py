class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = defaultdict(int)
        longest = 0

        for num in nums:
            if length[num]:
                continue

            left = length[num - 1]
            right = length[num + 1]
            total = left + right + 1

            length[num] = length[num - left] = length[num + right] = total
            longest = max(longest, total)

        return longest
        