class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        r = [0] * l
        for i in range(l):
            p = 1
            for j in range(l):
                if i == j:
                    continue
                p *= nums[j]
            r[i] = p
        return r