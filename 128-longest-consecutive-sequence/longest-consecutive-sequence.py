class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        considered = set()
        starts = dict()
        ends = dict()
        
        ans = 1
        if len(nums)==0:
            return 0
        
        for n in nums:
            if n in considered:
                continue
            
            considered.add(n)
            if n-1 in ends and n+1 in starts:
                new_start = ends[n-1]
                new_end = starts[n+1]                
                del ends[n-1]
                del starts[n+1]
                
                starts[new_start] = new_end
                ends[new_end] = new_start

                ans = max(ans, new_end - new_start +1 )
            
            elif n-1 in ends:
                start = ends[n-1]
                starts[start] = n
                ends[n] = start

                del ends[n-1]

                ans = max(ans, n - start + 1)
        
            elif n+1 in starts:
                end = starts[n+1]
                ends[end] = n
                starts[n] = end

                del starts[n+1]
                ans = max(ans, end - n + 1)
            
            else:
                starts[n] = n
                ends[n] = n
        
        return ans 