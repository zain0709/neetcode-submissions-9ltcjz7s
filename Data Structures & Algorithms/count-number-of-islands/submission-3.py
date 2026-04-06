class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited= set()
        island = 0

        def bfs(row,col):
            queue = deque()
            visited.add((row, col))
            queue.append((row, col))
            directions = [ [1, 0] , [0,1] , [-1, 0], [0,-1]]
            while queue:
                row, col = queue.pop()

                for direction in directions:
                    rd, cd  = row + direction[0] , col + direction[1]
                    if  0 <= rd < rows and 0 <= cd < cols:
                        if grid[rd][cd]  == "1" and (rd,cd) not in visited:
                            queue.append((rd, cd))
                            visited.add((rd, cd))
            return 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)

                    island += 1
        return island