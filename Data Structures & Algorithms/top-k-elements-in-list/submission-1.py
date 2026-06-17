class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:     
        cache = {}
        arr = []
        result = []

        for n in nums:
            cache[n] =  cache.get(n, 0) + 1

        for n, i in cache.items():
            arr.append([i, n])
            
        arr.sort()


        while len(result) < k:
            result.append(arr.pop()[1])

        return result