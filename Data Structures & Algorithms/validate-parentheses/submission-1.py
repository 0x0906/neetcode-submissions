class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = { ")" : "(", "]" : "[", "}" : "{" }
        
        for d in s:
            if d in "({[":
                stack.append(d)
            else:
                if not stack:
                    return False
                    
                if stack.pop() != dic[d]:
                    return False

        return len(stack) == 0