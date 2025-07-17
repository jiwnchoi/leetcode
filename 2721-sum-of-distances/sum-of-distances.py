from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        num_to_indices = defaultdict(list)
        index_to_dist = defaultdict(int)

        for i, num in enumerate(nums):
            if num_to_indices[num]:
                last_index = num_to_indices[num][-1]
                index_to_dist[i] += (i - last_index) * len(num_to_indices[num]) + index_to_dist[last_index]
            num_to_indices[num].append(i)
        
        num_to_indices2 = defaultdict(list)
        index_to_dist2 = defaultdict(int)

        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            if num_to_indices2[num]:
                last_index = num_to_indices2[num][-1]
                index_to_dist2[i] += (last_index - i) * len(num_to_indices2[num]) + index_to_dist2[last_index]
                index_to_dist[i] += index_to_dist2[i]

            num_to_indices2[num].append(i)


        # print(num_to_indices, index_to_dist)
        return [
            index_to_dist.get(i, 0) for i in range(len(nums))
        ]


