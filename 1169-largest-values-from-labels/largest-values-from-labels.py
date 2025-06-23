from collections import defaultdict

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        vnl = [
            (v, l)
            for v, l in zip(values, labels)
        ]
        vnl = sorted(vnl, key= lambda x : x[0], reverse=True)

        limits = defaultdict(int)
        n = 0
        result = 0

        for v, l in vnl:
            if n == numWanted:
                break

            if limits[l] < useLimit:
                result += v
                limits[l] += 1
                n +=1 
        
        return result