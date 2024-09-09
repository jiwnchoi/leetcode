from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        computed = set(range(len(isConnected)))
        output = 1

        stack = [0]

        while len(stack) and len(computed):
            idx = stack.pop()
            computed -= {idx}

            for i in range(0, len(isConnected)):
                if isConnected[idx][i] == 1 and i in computed:
                    stack.append(i)

            
            if len(stack) == 0:
                for c in computed:
                    output += 1
                    stack.append(c)
                    break

        return output