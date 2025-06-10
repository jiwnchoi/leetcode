class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        
        dpA = [ 0 for _ in energyDrinkB]
        dpB = [ 0 for _ in energyDrinkB ]
        dpA[0] = energyDrinkA[0]
        dpA[1] = energyDrinkA[0] + energyDrinkA[1]
        dpB[0] = energyDrinkB[0]
        dpB[1] = energyDrinkB[0] + energyDrinkB[1]

        for i in range(2, len(energyDrinkA)):
            dpA[i] = max(dpA[i-1], dpB[i-2]) + energyDrinkA[i]
            dpB[i] = max(dpB[i-1], dpA[i-2]) + energyDrinkB[i]
        
        return max(dpA[-1], dpB[-1])