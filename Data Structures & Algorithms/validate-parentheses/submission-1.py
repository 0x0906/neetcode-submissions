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


# ([{ -> push it onto the stack.
# }]) -> check whether it matches the most recent opening bracket.

# stack = []

# '{' -> push
# stack = ['{']

# '[' -> push
# stack = ['{', '[']

# ']' -> matches '['
# stack = ['{']

# '}' -> matches '{'
# stack = []
