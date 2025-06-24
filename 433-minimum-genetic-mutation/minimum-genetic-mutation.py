from functools import cache
from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        @cache
        def f(g1, g2):
            cnt = 0
            for c1, c2 in zip(g1, g2):
                if c1 != c2:
                    cnt += 1
            return cnt 

        output = None

        queue = deque([(startGene, 0, [startGene])])

        while queue:
            current, cost, path = queue.popleft()
            if current == endGene:
                output = cost if output is None else min(output, cost)
            
            else:
                for gene in bank:
                    if gene not in path and f(current, gene) == 1:                    
                        queue.append((gene, cost+ f(current, gene), [*path, gene]))

        return -1 if output is None else output

            