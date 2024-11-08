from math import ceil, floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            if token == "*":
                n = stack.pop()
                current = stack.pop()
                stack.append(current * n)

            elif token == "/":
                n = stack.pop()
                current = stack.pop()
                
                result = current / n
                result = floor(result) if result > 0 else ceil(result)
                stack.append(result)

            elif token == "+":
                n = stack.pop()
                current = stack.pop()
                stack.append(n+current)
                
                

            elif token == "-":
                n = stack.pop()
                current = stack.pop()
                stack.append(current - n)

            else:
                stack.append(int(token))
        return stack[0]
            
