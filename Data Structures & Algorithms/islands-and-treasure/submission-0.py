class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        cols = len(grid[0])
        visited = set()
        queue = deque()
        def bfs():
            directions = [[1,0], [-1,0], [0,1], [0, -1]]
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr in range(row) and nc in range(cols) and grid[nr][nc] == 2147483647 and (nr,nc) not in visited:
                        grid[nr][nc]  = grid[r][c] + 1
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        
               
        for r in range(row):
            for c in range(cols):
                if grid[r][c] == 0 and (r,c) not in visited:
                    queue.append((r,c))
                    visited.add((r,c))
        bfs()
