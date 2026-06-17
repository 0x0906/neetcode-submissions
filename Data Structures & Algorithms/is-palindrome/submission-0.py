class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            while l < r and not s[l].isalnum(): # forward
                l += 1
            while r > l and not s[r].isalnum(): # backward
                r -= 1
            
            if s[l].lower() != s[r].lower(): # check each and every chars
                return False
                
            l += 1 # forward
            r -= 1 # backward
        
        # l == r pointers become equals and while stops
        return True 