class Solution(object):
    def wallsAndGates(self, rooms):
        rows = len(rooms)
        cols = len(rooms[0])
        q = deque([])
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r,c,0))
        while(q):
            r, c, dist = q.popleft()
            if(r >= 0 and r < rows and c >= 0 and c < cols
                and (r,c) not in visited and rooms[r][c] != -1):
                visited.add((r,c))
                q.append((r+1,c,dist+1))
                q.append((r-1,c,dist+1))
                q.append((r,c+1,dist+1))
                q.append((r,c-1,dist+1))
                rooms[r][c] = min(rooms[r][c], dist)
        return rooms
                    
                


        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        
