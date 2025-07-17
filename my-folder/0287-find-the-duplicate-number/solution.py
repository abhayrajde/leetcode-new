class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # How can we prove that cycle's start point is repeating char:
        # 2 * Slow = Fast
        # 2 * (P + C - X) = P + 2C - X | P = previos nodes, C = Cycles, X = remaining nodes(from meeting point to start of cycle)
        # 2P + 2C - 2X = P + 2C - X
        # P - X = 0
        # P = X

        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow

