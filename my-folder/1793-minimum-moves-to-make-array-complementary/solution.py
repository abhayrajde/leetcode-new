class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        # possible sums: 2 -> 2*limit
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):

            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit
            pair_sum = a + b

            # assume 2 moves for all sums
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            # sums needing only 1 move
            diff[low] -= 1
            diff[high + 1] += 1

            # exact sum needing 0 moves
            diff[pair_sum] -= 1
            diff[pair_sum + 1] += 1

        ans = float('inf')
        current = 0

        # build actual costs using prefix sum
        for s in range(2, 2 * limit + 1):
            current += diff[s]
            ans = min(ans, current)

        return ans
