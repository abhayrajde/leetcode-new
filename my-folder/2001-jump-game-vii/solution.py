from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # If the last character is '1', we can never reach it
        if s[-1] == '1':
            return False
            
        queue = deque([0])
        # Track the furthest index we've considered adding to the queue
        far_visited = 0 
        
        while queue:
            curr = queue.popleft()
            
            if curr == len(s) - 1:
                return True
            
            # Define the window of valid jumps from the current position
            start = max(curr + minJump, far_visited + 1)
            end = min(curr + maxJump, len(s) - 1)
            
            for i in range(start, end + 1):
                if s[i] == '0':
                    queue.append(i)
            
            # Update far_visited so the next iterations don't re-scan these indices
            far_visited = max(far_visited, curr + maxJump)
            
        return False
