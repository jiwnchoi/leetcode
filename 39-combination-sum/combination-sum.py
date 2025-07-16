class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() 
        result = []

        def backtrack(start_index, path, remain):
            if remain == 0:
                result.append(path[:]) 
                return

            for i in range(start_index, len(candidates)):
                current_num = candidates[i]

                if current_num > remain:
                    break 

                path.append(current_num)
                backtrack(i, path, remain - current_num)
                path.pop()

        backtrack(0, [], target)
        return result