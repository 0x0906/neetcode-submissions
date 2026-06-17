class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = []
        for n in nums:
            if n in l:
                return True
            l.append(n)
        return False