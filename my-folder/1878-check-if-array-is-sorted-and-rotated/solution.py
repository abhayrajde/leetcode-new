class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        
        counter = 1

        if N == 1: return True
        for i in range(1, N * 2):
            # prev, curr = (i - 1) % N, i % N
            if nums[(i - 1) % N] <= nums[i % N]:
                counter += 1
            else:
                counter = 1
            if counter == N:
                return True
        return False
            
