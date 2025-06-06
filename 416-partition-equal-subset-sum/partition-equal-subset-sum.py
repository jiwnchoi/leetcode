class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False 

        target = total // 2
        sums = set([0])

        for num in nums:
            new_sum = set()                
            for s in sums:
                if s + num == target:
                    return True
                elif s + num < target:
                    new_sum.add(s + num)
            sums = sums | new_sum
        return False
            


        