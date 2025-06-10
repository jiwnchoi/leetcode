class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        argmin_v = -1
        min_v = 1e5

        current = 0 

        for i, g in enumerate(gas):
            current += g - cost[i]
            if current < min_v:
                min_v = current
                argmin_v = i

        if current < 0:
            return -1 

        return (argmin_v + 1) % len(gas)
        