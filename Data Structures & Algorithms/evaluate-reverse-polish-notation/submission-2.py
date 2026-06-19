class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop()) # a + b
            elif t == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a) # b - a
            elif t == "*":
                stack.append(stack.pop() * stack.pop()) # a * b
            elif t == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b) / a)) # b / a (integers always truncates toward zero)
            else:
                stack.append(int(t))
        
        return stack[-1] 