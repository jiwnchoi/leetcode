class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner_0_indexed = 0 
        
        for i in range(2, n + 1):
            winner_0_indexed = (winner_0_indexed + k) % i
            
        return winner_0_indexed + 1