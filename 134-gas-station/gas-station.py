class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sc = sum(cost)
        sg = sum(gas)
        if sc > sg:
            return -1
        
        net = [
            gas[i] - cost[i]
            for i in range(len(gas))
        ]

        print(net)

        argmin_v = -1
        min_v = 1e5

        current = 0 

        for i, v in enumerate(net):
            current += v
            if current < min_v:
                min_v = current
                argmin_v = i

        return (argmin_v + 1) % len(gas)
        