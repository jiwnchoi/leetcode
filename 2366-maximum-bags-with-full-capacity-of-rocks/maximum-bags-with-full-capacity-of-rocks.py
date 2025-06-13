class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        sub = sorted([
            capacity[i] - rocks[i]
            for i in range(len(rocks))
        ])

        output = 0

        for s in sub:
            if additionalRocks >= s:
                additionalRocks -= s
                output += 1
            
            else:
                break

        return output



        