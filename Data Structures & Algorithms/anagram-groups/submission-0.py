class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = defaultdict(list)
        for s in strs:
            sortd = ''.join(sorted(s))
            r[sortd].append(s)
        return list(r.values())
            