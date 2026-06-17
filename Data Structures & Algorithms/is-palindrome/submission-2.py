class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            while l < r and not s[l].isalnum(): # if s[l] is not alphanum then move forward until we see alphanum
                l += 1
                continue
            while r > l and not s[r].isalnum(): # if s[r] is not alphanum then move backward until we see alphanum
                r -= 1
                continue
            
            if s[l].lower() != s[r].lower(): # check each and every chars
                return False
                
            l += 1 # forward
            r -= 1 # backward
        
        # l == r pointers become equals and while stops
        return True 