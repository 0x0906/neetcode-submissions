class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
    
            while l < r:
                a = nums[i] + nums[l] + nums[r]
                if a > 0:
                    r -= 1 
                elif a < 0:
                    l += 1
                else:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                    r -= 1
                
        return [list(x) for x in res]