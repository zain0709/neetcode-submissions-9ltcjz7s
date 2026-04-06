class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, cols = len(grid), len(grid[0])
        queue = deque()
        minutes = 0
        good = 0
        def bfs():
            nonlocal minutes
            nonlocal good
            directions = [[1,0], [-1,0], [0,1], [0, -1]]
            while queue:
                    length = len(queue)
                    for _ in range(length):
                        r, c = queue.popleft()
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if nr in range(row) and nc in range(cols) and grid[nr][nc] == 1:
                                grid[nr][nc] = 2
                                good -= 1
                                queue.append((nr, nc))
                    if queue:
                        minutes += 1
                

            return minutes if good == 0 else -1
        
        for r in range(row):
            for c in range(cols):
                if grid[r][c] == 1:
                    good += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
        return bfs()