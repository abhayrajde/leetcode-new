import random
class Solution:
    nums = []
    weighted_indexes = []
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sums.append(total)
        self.total_sum = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        # Perform binary search to find the correct index
        left, right = 0, len(self.prefix_sums) - 1
        while left < right:
            mid = (left + right) // 2
            if self.prefix_sums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
