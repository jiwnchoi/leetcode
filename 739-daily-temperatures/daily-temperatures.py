class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]
        output = [0 for _ in temperatures]

        for i, temp in enumerate(temperatures):
            if i == 0:
                continue
            
            while len(stack) and temp > stack[-1][0]:
                c = stack.pop()
                output[c[1]] = i - c[1]
            
            stack.append((temp, i))
        
        return output