class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {0: -1}

        max_length = 0
        num_ones = 0
        num_zeros = 0
        
        for i, num in enumerate(nums):
            if num == 1:
                num_ones +=1
            else:
                num_zeros += 1

            value = num_ones - num_zeros
            if value in hashmap:

                max_length = max(max_length, i-hashmap[value])
            else:
                hashmap[value] = i


        return max_length


