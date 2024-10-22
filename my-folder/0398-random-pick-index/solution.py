import random
class Solution:

    def __init__(self, nums: List[int]):
        self.cache = {}
        for i, n in enumerate(nums):
            if n in self.cache:
                self.cache[n].append(i)
            else:
                self.cache[n] = [i]
                
    def pick(self, target: int) -> int:
        ran = random.randint(0, len(self.cache[target])- 1)
        return self.cache[target][ran]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
