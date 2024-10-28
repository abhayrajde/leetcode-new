class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def can_cut(length):
            count = 0
            for ribbon in ribbons:
                count += ribbon // length
            return count
        
        left, right = 1, max(ribbons)
        best_length = 0

        while left <= right:
            mid = (left + right) // 2
            if can_cut(mid) >= k:
                best_length = mid  # Update the best length found so far
                left = mid + 1  # Try a longer length
            else:
                right = mid - 1  # Try a shorter length

        return best_length
