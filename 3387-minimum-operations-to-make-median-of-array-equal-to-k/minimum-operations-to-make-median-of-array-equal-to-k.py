from bisect import bisect_left

class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)

        med_index = len(nums)// 2 

        x = bisect_left(nums, k)
        

        med_value = nums[med_index]

        ans = 0
        start = min(x, med_index)
        end = max(x, med_index+1) 
        for i in range(start, end):
            ans += abs(nums[i] - k)
            nums[i] -= (nums[i] - k)
        return ans


