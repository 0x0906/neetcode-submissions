class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 1
                current = n
                while current + 1 in numSet:
                    current += 1
                    length += 1
                longest = max(longest, length)

        return longest